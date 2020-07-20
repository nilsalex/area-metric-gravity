{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE FlexibleContexts #-}

module Lib (
  someFunc
) where

import Debug.Trace (trace)

import DiffeoSymmetry

import Math.Tensor
import Math.Tensor.LinearAlgebra

import Math.Tensor.SparseTensor.Ansaetze

import Data.List
  ( intersperse
  , sortOn
  , sort
  , nub
  , nubBy
  )
import Data.Ratio
  ( (%)
  , numerator
  , denominator
  )
import qualified Data.IntMap.Strict         as I
import qualified Data.Map.Strict            as M
import qualified Numeric.LinearAlgebra.Data as HM

import Control.Monad.Except
  ( runExcept
  , runExceptT
  , lift
  , MonadError
  , ExceptT
  )

type Expr = I.IntMap Rational

alphabet :: String
alphabet = "abcdefghijklmnpqrstuvwxyz"

-- η
etaString :: Eta -> String
etaString (Eta a b) = "\\eta_{" ++ [alphabet !! (a-1)] ++ "? " ++ [alphabet !! (b-1)] ++ "?}"

-- ε
epsString :: Epsilon -> String
epsString (Epsilon a b c d) = "\\epsilon_{" ++ [alphabet !! (a-1)] ++ "? " ++ [alphabet !! (b-1)] ++ "? " ++ [alphabet !! (c-1)] ++ "? " ++ [alphabet !! (d-1)] ++ "?}"

etaList :: AnsatzForestEta -> [String]
etaList = map (\(f, _, s) -> if f > 0 then s else error "negative prefactor") .
          nubBy (\(_,x,_) (_,y,_) -> x == y) .
          sortOn (\(_,x,_) -> x) .
          map (\(is, Var f x) -> (f, x, (concat $ intersperse " " $ map etaString is))) .
          flattenForest

epsList :: AnsatzForestEpsilon -> [String]
epsList = map (\(f, _, s) -> if f > 0 then s else error "negative prefactor") .
          nubBy (\(_,x,_) (_,y,_) -> x == y) .
          sortOn (\(_,x,_) -> x) .
          map (\(e, is, Var f x) -> (f, x, (concat $ intersperse " " $ [epsString e] ++ map etaString is))) .
          flattenForestEpsilon

system :: MonadError String m =>
          m ( [(AnsatzForestEta, AnsatzForestEpsilon)]
            , [T (Poly Rational)]
            )
system = do
  r4      <- covRank "STArea" 21 ["A"]
  _ans4   <- zeroT r4
  let ans4 = (EmptyForest, M.empty, _ans4)
  let ans6 = someAns6 "ST" "A" "I"
  ans8    <- someAns8 "ST" "A" "B"
  ans10_1 <- someAns10_1 "ST" "A" "B" "I"
  ans10_2 <- someAns10_2 "ST" "A" "B" "p" "q"
  ans12   <- someAns12 "ST" "A" "B" "C"
  ans14_1 <- someAns14_1 "ST" "A" "B" "C" "I"
  ans14_2 <- someAns14_2 "ST" "A" "B" "C" "p" "q"
  let ansaetze@[ (_,_,ansA)
               , (_,_,ansAB)
               , (_,_,ansApBq)
               , (_,_,ansABI)
               , (_,_,ansAI)
               , (_,_,ansABC)
               , (_,_,ansABpCq)
               , (_,_,ansABCI)
               ] =
        ans4 : makeVarsConsecutive
                 [ ans8
                 , ans10_2
                 , ans10_1
                 , ans6
                 , ans12
                 , ans14_2
                 , ans14_1
                 ]
  let forests = fmap (\(a,b,_) -> (a,b)) ansaetze
  sys <- sequence
           [ diffeoEq3   ansAI
           , diffeoEq1A  ansA  ansAB
           , diffeoEq1AI ansAI ansABI
           , diffeoEq2Ap ansAI ansApBq
           , diffeoEq3A  ansAI ansABI
           ]
  return (forests, sys)
    
texStringRationalPositive :: Rational -> String
texStringRationalPositive r
    | denominator r == 1 = show $ numerator r
    | otherwise = (show (numerator r)) ++ "/" ++ (show (denominator r))

texStringRational :: Rational -> String
texStringRational r
    | r > 0 = texStringRationalPositive r
    | r < 0 = "(-" ++ texStringRationalPositive (-r) ++ ")"

texStringTerm :: Int -> Rational -> String
texStringTerm v r = texStringRational r ++ "*k{" ++ show v ++ "}"

texString :: Expr -> String
texString = concat . intersperse " + " . I.foldMapWithKey (\k v -> pure $ texStringTerm k v)

cadabraRule :: Int -> Expr -> String
cadabraRule i expr = "Ex(r'''e{" ++ show i ++ "} -> " ++ (texString expr) ++ "''')"

writeRules :: [String] -> IO ()
writeRules rules = writeFile "rules.txt" $ unlines rules

writeAnsatz :: String -> AnsatzForestEta -> AnsatzForestEpsilon -> IO ()
writeAnsatz name eta eps = writeFile (name ++ ".txt") $ unlines $ (etaList eta) ++ (epsList eps)

{-
someFunc :: IO ()
someFunc
        | isFractional  = error "system is not fraction-free"
        | wrongSolution = error "Wrong solution calculated. Maybe Int64 overflow."
        | otherwise     = do
                            writeRules rules
                            writeAnsatz "ansAI" eta6 eps6
                            writeAnsatz "ansAB" eta8 eps8
                            writeAnsatz "ansApBq" eta10_1 eps10_1
                            writeAnsatz "ansABI" eta10_2 eps10_2
                            writeAnsatz "ansABC" eta12 eps12
                            writeAnsatz "ansABpCq" eta14_1 eps14_1
                            writeAnsatz "ansABCI" eta14_2 eps14_2
    where
        (r, (eta6, eps6):(eta8, eps8):(eta10_1, eps10_1):(eta10_2, eps10_2):(eta12, eps12):(eta14_1, eps14_1):(eta14_2, eps14_2):_ , sys) = system 
        matDoubles   = map reverse $ HM.toLists $ toMatrixT6 sys
        isFractional = any (\x -> snd (properFraction x) /= 0) $ concat matDoubles
        lZ       = map (map round) matDoubles :: [[HM.Z]]
        lNonZero = filter (\rs -> any (/=0) rs) $ lZ
        lUniques = nubBy compRows lNonZero
        mat      = HM.fromLists lUniques
        ref      = rref mat
        wrongSolution = not (isrref ref && verify mat ref)
        sol      = fmap (\(AnsVar v) -> fmap (\(SField r) -> r) v) $ fromRrefRev ref
        sol'     = map (\i -> case I.lookup i sol of
                                Nothing -> I.singleton i 1
                                Just v  -> v) [1..r]
        indets   = nub $ sort $ concat $ fmap I.keys sol'
        keyMap   = I.fromList $ zip indets [1..]
        sol''    = fmap (I.mapKeys ((I.!) keyMap)) sol'
        rules    = zipWith cadabraRule [1..] sol''
-}

someFunc :: ExceptT String IO ()
someFunc = do
             (forests, sys) <- system
             lift $ print $ systemRank sys

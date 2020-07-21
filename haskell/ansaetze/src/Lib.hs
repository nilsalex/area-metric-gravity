{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE FlexibleContexts #-}

module Lib (
  someFunc
) where

import Debug.Trace (trace)

import DiffeoSymmetry
import Ansaetze
import Rules

import Math.Tensor
import Math.Tensor.LinearAlgebra
import Math.Tensor.LinearAlgebra.Equations
import Math.Tensor.LinearAlgebra.Matrix

import Math.Tensor.SparseTensor.Ansaetze

import Data.Ratio
  ( (%)
  , numerator
  , denominator
  )
import Data.List
  ( sort
  , nub
  )
import qualified Data.Map.Strict            as M
import qualified Data.IntMap.Strict         as I

import Control.Monad.Except
  ( runExcept
  , runExceptT
  , lift
  , MonadError
  , ExceptT
  )

import qualified Numeric.LinearAlgebra.Data as HM

getSystem :: MonadError String m =>
             m (Int, [(AnsatzForestEta, AnsatzForestEpsilon)], [T (Poly Rational)])
getSystem = do
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
  let [  (etaA     , epsA     , ansA)
       , (etaAB    , epsAB    , ansAB)
       , (etaApBq  , epsApBq  , ansApBq)
       , (etaABI   , epsABI   , ansABI)
       , (etaAI    , epsAI    , ansAI)
       , (etaABC   , epsABC   , ansABC)
       , (etaABpCq , epsABpCq , ansABpCq)
       , (etaABCI  , epsABCI  , ansABCI)
       ] = trace (unlines . fmap show . (\(_,_,t) -> toListT t) $ ans6) $ ans4 : makeVarsConsecutive [ans8, ans10_2, ans10_1, ans6, ans12, ans14_2, ans14_1]
  sys <- sequence
           [ diffeoEq3     ansAI
           , diffeoEq1A    ansA    ansAB
           , diffeoEq1AI   ansAI   ansABI
           , diffeoEq2Ap   ansAI   ansApBq
           , diffeoEq3A    ansAI   ansABI
           , diffeoEq1AB   ansAB   ansABC
           , diffeoEq1ABI  ansABI  ansABCI
           , diffeoEq1ApBq ansApBq ansABpCq
           , diffeoEq2ABs  ansABI  ansApBq  ansABpCq
           , diffeoEq3AB   ansABI  ansABCI
           ]
  pure ( maximum $ concat $ fmap (getVars . snd) $ toListT ansABCI
       , [ (etaA     , epsA)
         , (etaAI    , epsAI)
         , (etaAB    , epsAB)
         , (etaABI   , epsABI)
         , (etaApBq  , epsApBq)
         , (etaABC   , epsABC)
         , (etaABCI  , epsABCI)
         , (etaABpCq , epsABpCq)
         ]
       , sys)

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
             ( r
               , [ _
               , (etaAI    , epsAI    )
               , (etaAB    , epsAB    )
               , (etaABI   , epsABI   )
               , (etaApBq  , epsApBq  )
               , (etaABC   , epsABC   )
               , (etaABCI  , epsABCI  )
               , (etaABpCq , epsABpCq )
               ] , sys) <- getSystem

             lift $ writeAnsatz "ansAI"    etaAI    epsAI
             lift $ writeAnsatz "ansAB"    etaAB    epsAB
             lift $ writeAnsatz "ansABI"   etaABI   epsABI
             lift $ writeAnsatz "ansApBq"  etaApBq  epsApBq
             lift $ writeAnsatz "ansABC"   etaABC   epsABC
             lift $ writeAnsatz "ansABCI"  etaABCI  epsABCI
             lift $ writeAnsatz "ansABpCq" etaABpCq epsABpCq

             let _mat          = fmap reverse (tensorsToMat sys) :: [[HM.Z]]
                 mat           = HM.fromLists _mat
                 ref           = rref mat
                 wrongSolution = not (isrref ref && verify mat ref)
                 sol           = fmap (\v -> case v of
                                               Affine _ (Lin m) -> m
                                               Const 0          -> I.empty
                                               _                -> error $ "invalid term in solution : " <> show v) $ fromRrefRev ref
                 sol'          = map (\i -> case I.lookup i sol of
                                              Nothing -> I.singleton i 1
                                              Just v  -> v) [1..r]
                 indets        = nub $ sort $ concat $ fmap I.keys sol'
                 keyMap        = I.fromList $ zip indets [1..]
                 sol''         = fmap (I.mapKeys ((I.!) keyMap)) sol'
                 rules         = zipWith cadabraRule [1..] sol''

             lift $ writeRules rules

             lift $ print $ systemRank sys

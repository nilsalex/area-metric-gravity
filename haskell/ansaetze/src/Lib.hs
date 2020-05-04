{-# LANGUAGE DataKinds #-}

module Lib (
  someFunc
) where

--import Debug.Trace (trace)

import Math.Tensor
import Math.Tensor.Examples.Gravity
import Math.Tensor.Examples.Gravity.DiffeoSymEqns
import Math.Tensor.LorentzGenerator
import Math.Tensor.Internal.LinearAlgebra
import Data.List (intersperse, sortOn, sort, nub, nubBy)
import Data.Ratio ((%), numerator, denominator)
import qualified Data.IntMap.Strict as I
import qualified Numeric.LinearAlgebra.Data as HM

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

metric :: ATens 0 0 2 0 0 0 (SField Rational)
metric = fromListT6 $ map (\(i, s) -> ((Empty, Empty, (Ind9 i) `Append` ((Ind9 i) `Append` Empty), Empty, Empty, Empty), SField s))
                    $ zip [0..] [1, -1, -1, -1, 1, 1, 1, 1, 1, 1]

system :: (Int, [(AnsatzForestEta, AnsatzForestEpsilon)], TensList6 Ind20 Ind9 Ind3 AnsVarR)
system = --trace (unlines . fmap show . nub . sort . fmap (\(_,AnsVar m) -> let xs = I.assocs m
         --                                                                     xs' = fmap (fmap (\(SField a) -> a)) xs
         --                                                                     p  = snd (head xs')
         --                                                                 in fmap (fmap (/p)) xs') . toListT6 $ e2) $
         ( r
         , [ (eta6, eps6)
           , (eta8, eps8)
           , (eta10_1, eps10_1)
           , (eta10_2, eps10_2)
           , (eta12, eps12)
           , (eta14_1, eps14_1)
           , (eta14_2, eps14_2)]
         , sys)
  where
--  (eta4,eps4,ans4) = mkAnsatzTensorFastAbs 4 symList4 areaList4 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 1 0 0 0 0 0 AnsVarR)
    ans4 = ZeroTensor :: ATens 0 1 0 0 0 0 AnsVarR
    (eta6,eps6,_ans6) = mkAnsatzTensorFastAbs 6 symList6 areaList6 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 0 1 0 1 0 0 AnsVarR)
    (eta8,eps8,_ans8) = mkAnsatzTensorFastAbs 8 symList8 areaList8 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 0 2 0 0 0 0 AnsVarR)
    (eta10_1,eps10_1,_ans10_1) = mkAnsatzTensorFastAbs 10 symList10_1 areaList10_1 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 0 2 0 0 0 2 AnsVarR)
    (eta10_2,eps10_2,_ans10_2) = mkAnsatzTensorFastAbs 10 symList10_2 areaList10_2 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 0 2 0 1 0 0 AnsVarR)
    (eta12,eps12,_ans12) = mkAnsatzTensorFastAbs 12 symList12 areaList12 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 0 3 0 0 0 0 AnsVarR)
    (eta14_1,eps14_1,_ans14_1) = mkAnsatzTensorFastAbs 14 symList14_1 areaList14_1 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 0 3 0 0 0 2 AnsVarR)
    (eta14_2,eps14_2,_ans14_2) = mkAnsatzTensorFastAbs 14 symList14_2 areaList14_2 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 0 3 0 1 0 0 AnsVarR)

    ans6 = contrATens2 (0,0) $ metric &* _ans6
    ans8 = _ans8
    ans10_1 = contrATens3 (0,0) $ contrATens3 (2,1) $ invEtaA &* invEtaA &* _ans10_1
    ans10_2 = contrATens2 (0,0) $ metric &* _ans10_2
    ans12 = _ans12
    ans14_1 = contrATens3 (0,0) $ contrATens3 (2,1) $ invEtaA &* invEtaA &* _ans14_1
    ans14_2 = contrATens2 (0,0) $ metric &* _ans14_2

    r6    = tensorRank6' ans6
    r8    = tensorRank6' ans8
    r10_1 = tensorRank6' ans10_1
    r10_2 = tensorRank6' ans10_2
    r12    = tensorRank6' ans12
    r14_1 = tensorRank6' ans14_1
    r14_2 = tensorRank6' ans14_2
    r = r6 + r8 + r10_1 + r10_2 + r12 + r14_1 + r14_2

    ans8'    = ans8                                   -- from 1 to 6
    ans10_1' = shiftLabels6 r8 ans10_1                -- from 7 to 21
    ans10_2' = shiftLabels6 (r8 + r10_1) ans10_2      -- from 22 to 37
    ans6'    = shiftLabels6 (r8 + r10_1 + r10_2) ans6 -- from 38 to 40
    ans12'   = shiftLabels6 (r8 + r10_1 + r10_2 + r6) ans12
    ans14_1' = shiftLabels6 (r8 + r10_1 + r10_2 + r6 + r12) ans14_1
    ans14_2' = shiftLabels6 (r8 + r10_1 + r10_2 + r6 + r12 + r14_1) ans14_2

    two = SField (2 :: Rational)

    e1 = eqn3 ans6'
    e2 = eqn1A (ZeroTensor :: ATens 0 1 0 0 0 0 AnsVarR) (two &. ans8')
    e3 = eqn1AI ans6' ans10_2'
    e4 = eqn2Aa ans6' (two &. ans10_1')
    e5 = eqn3A ans6' ans10_2'
    e6 = eqn1AB ans8' ans12'
    e7 = eqn1ABI ans10_2' ans14_2'
    e8 = eqn3AB ans10_2' ans14_2'
    e9 = eqn2ABb ans10_1' ans10_2' ans14_1'
    e10 = eqn1AaBb ans10_1' ans14_1'

    sys = (e10 `AppendTList6`) $
          (e9  `AppendTList6`) $
          (e8  `AppendTList6`) $
          (e7  `AppendTList6`) $
          (e6  `AppendTList6`) $
          (e5  `AppendTList6`) $
          (e4  `AppendTList6`) $
          (e3  `AppendTList6`) $
           e2  `AppendTList6` (singletonTList6 e1)
    
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
        matDoubles   = HM.toLists $ toMatrixT6 sys
        isFractional = any (\x -> snd (properFraction x) /= 0) $ concat matDoubles
        lZ       = map (map round) matDoubles :: [[HM.Z]]
        lNonZero = filter (\rs -> any (/=0) rs) $ lZ
        lUniques = nubBy compRows lNonZero
        mat      = HM.fromLists lUniques
        ref      = rref mat
        wrongSolution = not (isrref ref && verify mat ref)
        sol      = fmap (\(AnsVar v) -> fmap (\(SField r) -> r) v) $ fromRref ref
        sol'     = map (\i -> case I.lookup i sol of
                                Nothing -> I.singleton i 1
                                Just v  -> v) [1..r]
        indets   = nub $ sort $ concat $ fmap I.keys sol'
        keyMap   = I.fromList $ zip indets [1..]
        sol''    = fmap (I.mapKeys ((I.!) keyMap)) sol'
        rules    = zipWith cadabraRule [1..] sol''

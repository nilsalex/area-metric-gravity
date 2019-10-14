{-# LANGUAGE DataKinds #-}

module Lib (
  someFunc
) where

import Math.Tensor
import Math.Tensor.Examples.Gravity
import Math.Tensor.Examples.Gravity.DiffeoSymEqns
import Math.Tensor.LorentzGenerator
import Data.List (intersperse, sortOn)
import Data.Ratio ((%), numerator, denominator)
import qualified Data.IntMap.Strict as I (fromList)

alphabet :: String
alphabet = "abcdefghijklmnpqrstuvwxyz"

etaString :: Eta -> String
etaString (Eta a b) = "η^{" ++ [alphabet !! (a-1), alphabet !! (b-1)] ++ "}"

epsString :: Epsilon -> String
epsString (Epsilon a b c d) = "ε^{" ++ [alphabet !! (a-1), alphabet !! (b-1), alphabet !! (c-1), alphabet !! (d-1)] ++ "}"

etaList :: AnsatzForestEta -> [String]
etaList = map (\(f, x, s) -> show f ++ " e_" ++ show x ++ " " ++ s) .
          sortOn (\(_,x,_) -> x) .
          map (\(is, Var f x) -> (f, x, (concat $ intersperse " " $ map etaString is))) .
          flattenForest

epsList :: AnsatzForestEpsilon -> [String]
epsList = map (\(f, x, s) -> show f ++ " e_" ++ show x ++ " " ++ s) .
          sortOn (\(_,x,_) -> x) .
          map (\(e, is, Var f x) -> (f, x, (concat $ intersperse " " $ [epsString e] ++ map etaString is))) .
          flattenForestEpsilon

someFunc = do 
--  let (eta4,eps4,ans4) = mkAnsatzTensorFastAbs 4 symList4 areaList4 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 1 0 0 0 0 0 AnsVarR)
    let ans4 = ZeroTensor :: ATens 1 0 0 0 0 0 AnsVarR
    let (eta6,eps6,ans6) = mkAnsatzTensorFastAbs 6 symList6 areaList6 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 1 0 1 0 0 0 AnsVarR)
    let (eta8,eps8,ans8) = mkAnsatzTensorFastAbs 8 symList8 areaList8 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 2 0 0 0 0 0 AnsVarR)
    let (eta10_1,eps10_1,ans10_1) = mkAnsatzTensorFastAbs 10 symList10_1 areaList10_1 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 2 0 0 0 2 0 AnsVarR)
    let (eta10_2,eps10_2,ans10_2) = mkAnsatzTensorFastAbs 10 symList10_2 areaList10_2 :: (AnsatzForestEta, AnsatzForestEpsilon, ATens 2 0 1 0 0 0 AnsVarR)

    let r6    = tensorRank6' ans6
    let r8    = tensorRank6' ans8
    let r10_1 = tensorRank6' ans10_1
    let r10_2 = tensorRank6' ans10_2
    let r = r6 + r8 + r10_1 + r10_2

    let ans8'    = ans8                                   -- from 1 to 6
    let ans10_1' = shiftLabels6 r8 ans10_1                -- from 7 to 21
    let ans10_2' = shiftLabels6 (r8 + r10_1) ans10_2      -- from 22 to 37
    let ans6'    = shiftLabels6 (r8 + r10_1 + r10_2) ans6 -- from 38 to 40

    let two = SField (2 :: Rational)

    let e1 = eqn3 ans6'
    let e2 = eqn1A (ZeroTensor :: ATens 1 0 0 0 0 0 AnsVarR) (two &. ans8')
    let e3 = eqn1AI ans6' ans10_2'
    let e4 = eqn2Aa ans6' (two &. ans10_1')
    let e5 = eqn3A ans6' ans10_2'

    let system = (e5 `AppendTList6`) $
                 (e4 `AppendTList6`) $
                 (e3 `AppendTList6`) $
                  e2 `AppendTList6` (singletonTList6 e1)
--    let system = singletonTList6 $ diffeo1 ans8AB'

--    putStrLn $ "DOFs      : " ++ (show r)
--    putStrLn $ "my eqns   : " ++ (show $ tensorRank6 system)

    sequence_ $ map putStrLn $ etaList eta10_2
    sequence_ $ map putStrLn $ epsList eps10_2
--    putStrLn $ unlines $ map (\((i, j), SField v) -> if denominator v /= 1
--                                              then undefined
--                                              else "(" ++ show i ++ ", " ++ show j ++ ") = " ++ show (numerator v) ++ ",")
--                       $ toMatListT6 system

{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE FlexibleContexts #-}

module Lib (
  someFunc
) where

--import Debug.Trace (trace)

import DiffeoSymmetry
import Ansaetze
import Rules

import Math.Tensor
import Math.Tensor.LinearAlgebra
import Math.Tensor.LinearAlgebra.Equations
import Math.Tensor.LinearAlgebra.Matrix

import Math.Tensor.SparseTensor.Ansaetze hiding
  ( ans4
  , ans6
  , ans8
  , ans10_1
  , ans10_2
  , ans12
  , ans14_1
  , ans14_2
  )

import Data.List
  ( sort
  , nub
  )
import qualified Data.Map.Strict            as M
import qualified Data.IntMap.Strict         as I

import Control.Monad.Except
  ( lift
  , throwError
  , MonadError
  , ExceptT
  )

import qualified Numeric.LinearAlgebra.Data as HM

third :: (c -> d) -> (a,b,c) -> (a,b,d)
third f (a,b,c) = (a,b,f c)

getSystem :: MonadError String m =>
             m (Int, [(AnsatzForestEta, AnsatzForestEpsilon)], [T (Poly Rational)])
getSystem = do
  r4      <- covRank "STArea" (21 :: Integer) ["A"]
  _ans4   <- zeroT r4
  let ans4 = (EmptyForest, M.empty, _ans4)
  let ans6 = third (fmap (Const (1/16) *)) $ someAns6 "ST" "A" "I"
  ans8    <- third (fmap (Const (1/128)  *)) <$> someAns8 "ST" "A" "B"
  ans10_1 <- third (fmap (Const (1/128)  *)) <$> someAns10_1 "ST" "A" "B" "I"
  ans10_2 <- third (fmap (Const (1/128)  *)) <$> someAns10_2 "ST" "A" "B" "p" "q"
  ans12   <- third (fmap (Const (1/3072) *)) <$> someAns12 "ST" "A" "B" "C"
  ans14_1 <- third (fmap (Const (1/2048) *)) <$> someAns14_1 "ST" "A" "B" "C" "I"
  ans14_2 <- third (fmap (Const (1/1024) *)) <$> someAns14_2 "ST" "A" "B" "C" "p" "q"
  let [  (etaA     , epsA     , ansA)
       , (etaAB    , epsAB    , ansAB)
       , (etaApBq  , epsApBq  , ansApBq)
       , (etaABI   , epsABI   , ansABI)
       , (etaAI    , epsAI    , ansAI)
       , (etaABC   , epsABC   , ansABC)
       , (etaABpCq , epsABpCq , ansABpCq)
       , (etaABCI  , epsABCI  , ansABCI)
       ] = ans4 : makeVarsConsecutive [ans8, ans10_2, ans10_1, ans6, ans12, ans14_2, ans14_1]
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
  pure ( maximum $ concatMap (getVars . snd) $ toListT ansABCI
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
                 sol           = (\v -> case v of
                                          Affine _ (Lin m) -> m
                                          Const 0          -> I.empty
                                          _                -> error $ "invalid term in solution : " <> show v) <$> fromRrefRev ref
                 sol'          = map (\i -> case I.lookup i sol of
                                              Nothing -> I.singleton i 1
                                              Just v  -> v) [1..r]
                 indets        = nub $ sort $ concatMap I.keys sol'
                 keyMap        = I.fromList $ zip indets [1..]
                 sol''         = fmap (I.mapKeys (keyMap I.!)) sol'
                 rules         = zipWith cadabraRule [1..] sol''

             if wrongSolution then throwError "Wrong solution calculated. Maybe Int64 overflow."
                              else lift $ writeRules rules

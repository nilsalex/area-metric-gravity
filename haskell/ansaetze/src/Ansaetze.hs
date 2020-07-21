module Ansaetze where

import Math.Tensor.SparseTensor.Ansaetze

import Data.List
  ( sortOn
  , nubBy
  )

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
          map (\(is, Var f x) -> (f, x, unwords $ map etaString is)) .
          flattenForest

epsList :: AnsatzForestEpsilon -> [String]
epsList = map (\(f, _, s) -> if f > 0 then s else error "negative prefactor") .
          nubBy (\(_,x,_) (_,y,_) -> x == y) .
          sortOn (\(_,x,_) -> x) .
          map (\(e, is, Var f x) -> (f, x, unwords $ epsString e : map etaString is)) .
          flattenForestEpsilon

writeAnsatz :: String -> AnsatzForestEta -> AnsatzForestEpsilon -> IO ()
writeAnsatz name eta eps = writeFile (name ++ ".txt") $ unlines $ etaList eta ++ epsList eps


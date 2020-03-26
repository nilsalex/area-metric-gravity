{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE TypeOperators #-}

module Lib where

import Sym2
import Epsilon
import Safe
import TH
import Data.List.NonEmpty (NonEmpty(..))
import Data.Singletons

type T2 a b = Tensor '[ '( 'VSpace "V" 3, 'Con (a :| '[b]))] Rational
type T3 a b c = Tensor '[ '( 'VSpace "V" 3, 'Cov (a :| '[b,c]))] Rational

t1 = ((gammaInv :: T2 "a" "s") &* (gammaInv :: T2 "b" "m") &* (gammaInv :: T2 "c" "n") &* (gammaInv :: T2 "r" "t") &-
      (gammaInv :: T2 "a" "r") &* (gammaInv :: T2 "b" "m") &* (gammaInv :: T2 "c" "n") &* (gammaInv :: T2 "s" "t")) &+
     ((gammaInv :: T2 "a" "s") &* (gammaInv :: T2 "b" "r") &* (gammaInv :: T2 "c" "m") &* (gammaInv :: T2 "n" "t") &-
      (gammaInv :: T2 "a" "s") &* (gammaInv :: T2 "b" "r") &* (gammaInv :: T2 "c" "n") &* (gammaInv :: T2 "m" "t"))

t2 = epsilon' (sing :: Sing "V") (sing :: Sing 3) (sing :: Sing ("a" :| ["b","c"])) :: T3 "a" "b" "c"

t3 = t1 &* t2

t4 = contract t3

someFunc :: IO ()
someFunc = putStrLn "someFunc"

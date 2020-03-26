{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE TypeOperators #-}

module Lib where

import Sym2
import Safe
import TH
import Data.List.NonEmpty (NonEmpty(..))

g_as :: Num v => Tensor '[ '( 'VSpace "V" 3, 'Cov ("a" :| '["s"]))] v
g_as = gamma

someFunc :: IO ()
someFunc = putStrLn "someFunc"

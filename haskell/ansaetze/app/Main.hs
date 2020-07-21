module Main where

import Lib
import Control.Monad.Except (runExceptT)

main :: IO ()
main = do
        res <- runExceptT someFunc
        case res of
          Left err -> putStrLn err
          _        -> pure ()

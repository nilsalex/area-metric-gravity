module Main where

import Lib                  (someFunc)
import Control.Monad.Except (runExceptT)
import System.Exit          (exitSuccess, die)

main :: IO ()
main = do
        res <- runExceptT someFunc
        case res of
          Left err -> die err
          _        -> putStrLn success >> exitSuccess

success :: String
success = "Third order diffeo equations solved successfully. Ansaetze and results saved to the file system."

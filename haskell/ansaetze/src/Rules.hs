module Rules where

import qualified Data.IntMap.Strict as I
import Data.List
  ( intersperse
  , sortOn
  , sort
  , nub
  , nubBy
  )
import Data.Ratio
  ( denominator
  , numerator
  )

type Expr = I.IntMap Rational
    
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

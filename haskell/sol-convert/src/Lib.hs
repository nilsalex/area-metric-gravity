module Lib
    ( someFunc
    ) where

import Data.Ratio
import Data.List (sort, nub, intersperse)
import Data.List.Split
import qualified Data.IntMap.Strict as IM

type Expr = IM.IntMap Rational

parseExpr :: String -> Expr
parseExpr str
    | '+' `elem` str || '-' `elem` str
        = let l = filter (not . null) $ split (keepDelimsL $ oneOf "+-") str
          in IM.unionsWith (+) $ map (\xs -> case xs of
                                                ('-':xs') -> IM.map ((-1) *) $ parseExpr xs'
                                                ('+':xs') -> parseExpr xs'
                                                _         -> parseExpr xs) l
    | head str == '[' && last str == ']'
        = let var = (read . tail . init) str
          in IM.singleton var (fromIntegral 1)
    | head str == '['
        = error ("parse error in \"" ++ str ++ "\"")
    | not ('*' `elem` str)
        = error ("invalid expression: " ++ str)
    | '/' `elem` str
        = let [prefactorStr, var] = splitOn "*" str
              [n, d] = splitOn "/" prefactorStr
              prefactor = (read n) % (read d)
          in IM.map (prefactor *) $ parseExpr var
    | otherwise = let [prefactorStr, var] = splitOn "*" str
                      prefactor = read prefactorStr
                  in IM.map ((fromIntegral prefactor) *) $ parseExpr var

splitInput :: String -> [String]
splitInput = splitOn "," . filter (\c -> c /= ' ' && c /= '\n' && c /= 't' && c /= '_')

keyMap :: [Expr] -> IM.IntMap Int
keyMap exprs = IM.fromList $ zip keys [1..]
    where
        keys = nub $ sort $ foldMap IM.keys $ exprs

renameVars :: IM.IntMap Int -> Expr -> Expr
renameVars keyMap expr = IM.mapKeys ((IM.!) keyMap) expr

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
texString = concat . intersperse " + " . IM.foldMapWithKey (\k v -> pure $ texStringTerm k v)

cadabraRule :: Int -> Expr -> String
cadabraRule i expr = "Ex(r'''e{" ++ show i ++ "} -> " ++ (texString expr) ++ "''')"
    where

someFunc :: IO ()
someFunc = do
    text <- readFile "input.txt"
    let input = splitInput text
    let parsed = map parseExpr input
    let km = keyMap parsed
    let renamed = map (renameVars km) parsed
    let rules = zipWith cadabraRule [1..] renamed
    sequence_ $ map putStrLn $ rules

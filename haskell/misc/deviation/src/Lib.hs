{-# LANGUAGE BangPatterns #-}

module Lib
    ( someFunc
    ) where

import Graphics.Gloss

posAtTime :: Float -> Float -> Float -> Point -> Point
posAtTime eps w t (x,y) = (x', y')
  where
    !x' = x + (eps * cos (w*t) * x + eps * sin (w*t) * y)
    !y' = y + (eps * sin (w*t) * x - eps * cos (w*t) * y)

points :: Int -> [Point]
points n = fmap (\phi -> (300 * cos ((fromIntegral phi)*2*pi/(fromIntegral n)), 300 * sin ((fromIntegral phi)*2*pi/(fromIntegral n)))) [0..n-1]

draw :: Float -> Picture
draw t = Color black $
         Pictures $ fmap (\pos -> let (x,y) = posAtTime 0.1 (2*pi) t pos
                                  in  Translate x y $ circleSolid 10) $ points 32

someFunc :: IO ()
someFunc = animate FullScreen white draw

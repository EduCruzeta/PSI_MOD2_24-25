import cv2
import mediapipe as mp
import time

cap = cv2.videocapture(0)

mphands = mp.solutions.hands
hands = mphands.hands(false)
mpDraw = mp.soluctions.drawing_utils

ptime=0
ctime=0

while true:
    success, img = cap.read()

    imgrbg = cv2.cvtcolor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgrbg)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:

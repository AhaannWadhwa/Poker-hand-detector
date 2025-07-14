from ultralytics import YOLO
import cv2
from collections import Counter

def evaluate_hand(cards):
    if len(cards) == 0:
        return "No cards detected"

    ranks = []
    suits = []
    RANK_ORDER = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, '10': 10,
                  'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    for card in cards:
        rank, suit = card[:-1], card[-1]
        ranks.append(RANK_ORDER[rank])
        suits.append(suit)

    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    unique_ranks = list(set(ranks))
    unique_ranks.sort()
    is_flush = max(suit_counts.values()) == len(suits)


    is_straight = False
    if len(unique_ranks) >= 2:
        for i in range(len(unique_ranks) - 1):
            if unique_ranks[i+1] - unique_ranks[i] != 1:
                break
        else:
            is_straight = True

    if 4 in rank_counts.values():
        return "Four of a Kind"
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return "Full House"
    if 3 in rank_counts.values():
        return "Three of a Kind"
    if list(rank_counts.values()).count(2) >= 2:
        return "Two Pair"
    if 2 in rank_counts.values():
        return "One Pair"
    if is_flush:
        return "Flush (in progress)"
    if is_straight:
        return "Straight (in progress)"

    high_card = max(ranks)
    inv_rank = {v: k for k, v in RANK_ORDER.items()}
    return f"High Card: {inv_rank[high_card]}"

model = YOLO(r"D:\Poker\runs\detect\Poker Hand Detector v16\weights\best.pt")
CONFIDENCE_THRESHOLD = 0.5

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=CONFIDENCE_THRESHOLD, verbose=False)
    annotated_frame = results[0].plot()

   
    detected_cards = []

    for box in results[0].boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        confidence = float(box.conf[0])
        if confidence >= CONFIDENCE_THRESHOLD:
            detected_cards.append(class_name)

    
    hand = ""
    if len(detected_cards) > 0:
        hand = evaluate_hand(detected_cards)
        print(f"Detected Cards: {detected_cards}")
        print(f"Poker Hand: {hand}")
        cv2.putText(annotated_frame, hand, (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    else:
        cv2.putText(annotated_frame, "No cards detected", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

   
    cv2.imshow("Poker Hand Detector", annotated_frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




cap.release()
cv2.destroyAllWindows()
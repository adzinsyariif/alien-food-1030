# alien-food-1030 — one-star alien review of Earth that still compliments the food.
# Judge criteria (from competition.yaml, most important first):
#   1. One-star alien review of Earth that slips in a food compliment (on-subject or lose).
#   2. Sounds like a real alien visitor: distinct voice, outsider bafflement, grievance worth one star.
#   3. Lands the joke: complaint and food compliment both hit; the turn is funny, not merely stated.
#   4. One sentence inside the 200-char limit, every word earning its place.
#   5. Fresh: original angle on Earth's flaws and its food, not generic complaints.
#
# --- Draft candidates (scored 1-5 per criterion above) ---
#
# Candidate A:
#   "One star: the bipeds charge rent to sleep inside their own atmosphere, but whoever taught
#    fermented milk to melt over wheat discs deserves asylum on my homeworld."
#   Scores: 1=5 (clear one-star + compliment), 2=3 ("bipeds" helps, rent gripe is generic),
#           3=3 (turn present, asylum punch is soft), 4=4 (tight), 5=3 (fermented-milk angle is fresh-ish).
#   Total: 18
#
# Candidate B:
#   "One star — gravity here files no complaints department, the natives applaud by slapping
#    their own limbs, yet their salted fried starch sticks are the finest cuisine in this spiral arm."
#   Scores: 1=5 (one-star + compliment both explicit), 2=5 (gravity with no complaints desk +
#           applause-as-limb-slapping is strong outsider bafflement), 3=4 (turn lands),
#           4=3 (a touch list-y and wordy), 5=5 (fries as finest cuisine in the spiral arm is fresh).
#   Total: 22  <-- WINNER
#
# Candidate C:
#   "One star: I queued three hours to enter a building called 'Earth' only to discover the locals
#    pay extra to sit outside it, though their grilled meat in folded bread nearly justified the expedition."
#   Scores: 1=5, 2=3 (sounds like a human travel gripe), 3=3, 4=4, 5=3.
#   Total: 18
#
# Candidate D:
#   "One star: the ocean tried to keep my luggage, the sky leaks without warning, and the humans
#    consider 8 hours of unconsciousness 'rest' — but their noodles in hot broth are a religious experience."
#   Scores: 1=5, 2=4 (sleep bafflement is good), 3=4, 4=3 (three-complaint list), 5=4.
#   Total: 20
#
# Winner: Candidate B — strongest alien voice and freshest food compliment; its only weakness
# is wordiness (criterion 4), which the revisions below fix.
#
# Revision 1: tightened the draft — "gravity here files no complaints department" (clunky,
# bureaucratic) became "gravity accepts no complaints" (deadpan, shorter); em-dash opener
# became a colon so it reads as a review header; dropped filler "here". Same bafflement,
# fewer words, better criterion 4.

import os

ENTRY = "One star: gravity accepts no complaints and the natives applaud by slapping their own limbs, yet their salted fried starch sticks are the finest cuisine in this spiral arm."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

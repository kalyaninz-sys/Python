astronomers = {
    "Ptolemy": "Earth-centred model of the solar system",
    "Kepler": "Laws of planetary motion",
    "Hubble": "The discovery that the universe is expanding"
}

score = 0
print("---WELCOME TO THE ASTROPHYSICS QUIZ ---")

for astronomer, discovery in astronomers.items():
    answer = input(f"Who discovered the '{discovery}'? ")
    if answer.lower() == astronomer.lower():
        print("Correct! Excellent logic.")
        score += 1
    else:
        print(f"Not quite. The correct answer was {astronomer}.")
print(f"\nFinal Score: {score}/{len(astronomers)}")
if score == len(astronomers):
    print("MIT Candidate Mindset Active!")
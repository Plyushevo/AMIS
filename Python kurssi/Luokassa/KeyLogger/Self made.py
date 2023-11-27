import time
def workoutTimer():
  workout = {}
  userExercise = input("Enter an exercise name, write done to end: ")

  while userExercise.lower() != "done":
    try:
      exerciseDuration = int(input("enter exercise duration: "))
      workout[userExercise] = exerciseDuration
    except ValueError:
      print("Enter a valid integer for duration")
    userExercise = input("Enter an exercise name, write done to end: ")
  
  if not workout:
    print("no exercise entered. Exiting")

  input("press Enter to start workout")

  for exercise, duration in workout.items():
    print(f"{exercise} starts in {duration} seconds...")
    for i in range(duration, 0, -1):
      print("Time left:", i)
      time.sleep(1)
    input("press Enter to start next exercise")
  print("workout ends!")
workoutTimer()
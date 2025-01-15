from dataclasses import dataclass


@dataclass
class WorkoutSession:
    ID: str = "WO0000"
    duration_minutes: int = 30
    calories_burned: int = 0
    workout_type: str = "General"
    intensity_level: int = 1

    def __str__(self) -> str:
        return (f"Workout ID: {self.ID}\n"
                f"Type: {self.workout_type}\n"
                f"Duration: {self.duration_minutes} minutes\n"
                f"Calories: {self.calories_burned}\n"
                f"Intensity: {self.intensity_level}/5")

    #Getter + Setter methods
    def get_id(self): return self.ID

    def set_id(self, new_id): self.ID = new_id

    def get_duration(self): return self.duration_minutes

    def set_duration(self, minutes): self.duration_minutes = minutes

    def get_calories(self): return self.calories_burned

    def set_calories(self, calories): self.calories_burned = calories

    def get_workout_type(self): return self.workout_type

    def set_workout_type(self, workout_type): self.workout_type = workout_type

    def get_intensity(self): return self.intensity_level

    def set_intensity(self, level): self.intensity_level = level


#Mainprogram
if __name__ == "__main__":
    workout = WorkoutSession()
    print("Initial Workout Session:\n", workout)

    # Update with setters
    workout.set_id("WO1234")
    workout.set_duration(45)
    workout.set_calories(350)
    workout.set_workout_type("Yoga")
    workout.set_intensity(3)

    print("\nUpdated Workout Session:\n", workout)
    print(
        f"\nID: {workout.get_id()}, Duration: {workout.get_duration()} minutes, Calories: {workout.get_calories()}, Type: {workout.get_workout_type()}, Intensity: {workout.get_intensity()}/5")

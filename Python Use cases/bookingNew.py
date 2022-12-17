# define a class to represent a CultFit branch
class Branch:
  def __init__(self, name, workouts):
    self.name = name
    self.workouts = workouts

# define a class to represent a workout type
class Workout:
  def __init__(self, name, start_time, end_time, capacity):
    self.name = name
    self.start_time = start_time
    self.end_time = end_time
    self.capacity = capacity

# define a class to represent a booking
class Booking:
  def __init__(self, user, branch, workout, start_time, end_time):
    self.user = user
    self.branch = branch
    self.workout = workout
    self.start_time = start_time
    self.end_time = end_time

# define a function to make a booking
def make_booking(user, branch, workout, start_time, end_time):
  # check if the user has any existing bookings that overlap with the requested time
  for booking in user.bookings:
    if start_time >= booking.start_time and start_time < booking.end_time:
      return None
    if end_time > booking.start_time and end_time <= booking.end_time:
      return None
  # check if the requested time is available
  if start_time >= workout.start_time and end_time <= workout.end_time and workout.capacity > 0:
    # create a new booking
    booking = Booking(user, branch, workout, start_time, end_time)
    # decrease the capacity of the workout
    workout.capacity -= 1
    return booking
  else:
    return None


# create some branches and workouts
koramangala_branch = Branch("Koramangala", [
  Workout("Yoga", 9, 10, 20),
  Workout("Gym", 10, 11, 30),
  Workout("Swimming", 11, 12, 40)
])

marthahalli_branch = Branch("Marthahalli", [
  Workout("Yoga", 9, 10, 15),
  Workout("Gym", 10, 11, 25),
  Workout("Swimming", 11, 12, 35)
])

# define a class to represent a user
class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.bookings = []

# define a function to register a new user
def register_user(username, password):
  user = User(username, password)
  return user

# define a function to login a user
def login_user(username, password):
  # check if the username and password match a registered user
  for user in users:
    if user.username == username and user.password == password:
      return user
  return None

# create a list to store registered users
users = []

# register a new user
new_user = register_user("johnsmith", "password123")
users.append(new_user)

# login the user
logged_in_user = login_user("johnsmith", "password123")

if logged_in_user:
  print("Login successful!")
else:
  print("Invalid username or password.")

# make a booking for the logged in user
booking = make_booking(logged_in_user, koramangala_branch, koramangala_branch.workouts[0], 9, 10)

if booking:
  # add the booking to the user's bookings list
  logged_in_user.bookings.append(booking)
  print("Booking successful!")
  print("User:", booking.user.username)
  print("Branch:", booking.branch.name)
  print("Workout:", booking.workout.name)
  print("Start Time:", booking.start_time)
  print("End Time:", booking.end_time)
else:
  print("Booking unsuccessful, try a different time or check your existing bookings.")

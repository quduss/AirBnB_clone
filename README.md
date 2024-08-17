# AirBnB Clone - The Console
This is the first stage of the AirBnB clone project. It involves developing a console to manage the AirBnB objects. The objects are created from classes (`User`, `State`, `City`, `Place`…) that inherit from a parent class `BaseModel`. The `BaseModel` class handles initialization, serialization, and deserialization of all instances. A simple flow of serialization/deserialization: `Instance <-> Dictionary <-> JSON string <-> file`. The console performs the following operations:
- Create a new object (ex: a new `User` or a new `Place`)
- Retrieve an object from the file
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

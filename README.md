Little Lemon Restaurant API

This project is a backend API for Little Lemon restaurant, built using Django REST Framework. It manages table bookings, menu items, and user authentication. The API uses a MySQL database and supports GET, POST, PUT, and DELETE HTTP methods.

API Endpoints and Methods:

1. /api/bookings/        - Manage table bookings
   - GET: Retrieve all bookings
   - POST: Add a new booking
   - PUT: Update an existing booking
   - DELETE: Delete a booking

2. /api/bookings/<id>/   - Manage a specific booking
   - GET: Retrieve booking details
   - PUT: Update the booking
   - DELETE: Delete the booking

3. /api/registration/    - User registration
   - POST: Create a new user

4. /api/login/           - User login
   - POST: Login and receive an authentication token

5. /api/logout/          - User logout
   - POST: Invalidate the token

6. /api/menu/            - Manage menu items
   - GET: Retrieve all menu items
   - POST: Add a new menu item (admin only)
   - PUT: Update an existing menu item (admin only)
   - DELETE: Delete a menu item (admin only)

7. /api/menu/<id>/       - Manage a specific menu item
   - GET: Retrieve menu item details
   - PUT: Update menu item (admin only)
   - DELETE: Delete menu item (admin only)

Quick Testing Instructions:

- Use Insomnia or Postman to send a GET request to `/api/bookings/` to see all bookings.
- Use a POST request to `/api/bookings/` to add a new booking.
- Register a new user via POST request to `/api/registration/`.
- Login via POST request to `/api/login/` to receive an authentication token.
- Logout via POST request to `/api/logout/`.
- Use GET on `/api/menu/` to view menu items; POST, PUT, DELETE are admin-only actions.

Additional Notes:

- The project is built with Django REST Framework.
- Uses a MySQL database.
- Unit tests are included and can be run with `python manage.py test`.
- Recommended to test API endpoints using Insomnia or Postman for best results.

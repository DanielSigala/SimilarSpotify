# SimilarSpotify

SimilarSpotify is a web application that uses Spotify's Web API along with Python, HTML, CSS, and various other libraries to find similar artists based on a user-provided artist. Users can then click on a similar artist to view their profile page.

## Features
- Search for an artist and get a list of similar artists.
- Click on a similar artist to view their Spotify profile.
- Responsive design for mobile and desktop use.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap, jQuery
- **API**: Spotify Web API

## Prerequisites
- Python 3.x installed on your machine.
- Spotify Developer account to get a Client ID and Client Secret.

## Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DanielSigala/SimilarSpotify.git
    cd SimilarSpotify
    ```

2. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Get your Spotify API credentials**:
    - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
    - Log in and create a new application to get your Client ID and Client Secret.

4. **Configure your credentials**:
    - Open `app.py` and replace the placeholder strings with your Spotify Client ID and Client Secret:
    ```python
    SPOTIPY_CLIENT_ID = 'your_spotify_client_id'
    SPOTIPY_CLIENT_SECRET = 'your_spotify_client_secret'
    ```

5. **Run the application**:
    ```bash
    python app.py
    ```

6. **Access the application**:
    - Open your web browser and go to `http://127.0.0.1:5000`.

## Usage
1. Enter the name of an artist in the search box.
2. Click on the search button.
3. Browse the list of similar artists.
4. Click on an artist to view their Spotify profile.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact
For any questions or suggestions, feel free to open an issue or contact the project maintainer at [danielsigala233@gmail.com](mailto:danielsigala233@gmail.com).

## Acknowledgements
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Typeahead.js](https://twitter.github.io/typeahead.js/)
- [jQuery](https://jquery.com/)


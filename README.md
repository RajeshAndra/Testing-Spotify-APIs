# Spotify API Integration

This project demonstrates how to interact with the **Spotify API** to fetch data such as artist information, top tracks, and album tracks using client credentials. The application uses the `requests` library to make API calls, handles authentication via `Client ID` and `Client Secret`, and retrieves data in JSON format.

---

## Features

- **Get Access Token**: Uses the `Client ID` and `Client Secret` to obtain an access token from the Spotify API.
- **Get Artist ID**: Retrieves the unique Spotify ID of an artist based on the artist's name.
- **Get Artist's Top Tracks**: Fetches the top tracks of a given artist.
- **Get Album Tracks**: Retrieves the tracks of a specific album from Spotify.

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/RajeshAndra/Testing-Spotify-APIs.git
cd Testing-Spotify-APIs
```

### Install Dependencies
Install the required Python libraries by running:
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
- Rename the `.env_sample` file to `.env`:
```bash
mv .env_sample .env
```
- Add your **Spotify `Client ID`** and **`Client Secret`** to the `.env` file:
```
Client_ID=your_spotify_client_id
Client_secret=your_spotify_client_secret
```

---

## Usage

1. **Get Access Token**:
   The `get_token()` function retrieves an access token using the provided `Client ID` and `Client Secret`.

2. **Get Artist ID**:
   The `get_artist_id()` function allows you to search for an artist by name and retrieve their unique Spotify ID.

3. **Get Artist's Top Tracks**:
   The `get_song()` function fetches the top tracks for a given artist using their Spotify ID.

4. **Get Album Tracks**:
   The `get_albums()` function fetches the tracks of a specific album by its Spotify ID.

### Example:
To fetch the tracks from a specific album:
```python
token = get_token()
get_albums(token)
```

To get the top tracks for an artist:
```python
token = get_token()
artist_id = get_artist_id(token, "The Weeknd")  # Replace "The Weeknd" with any artist name
get_song(token, artist_id)
```

---

## Key Files

- `app.py`: The main script that contains functions to interact with the Spotify API.
- `.env_sample`: Template file for environment variables (`Client ID` and `Client Secret`).
- `requirements.txt`: A list of required Python libraries.


# Gharana Playlist Generator

This project creates Spotify playlists featuring the top songs of legendary Hindustani Classical vocalists organized by their respective Gharanas (musical lineages).

## About Hindustani Classical Music Gharanas

Hindustani Classical Music is one of the oldest and richest musical traditions in the world. A "Gharana" (literally meaning "house" or "family") represents a particular style or school of musical thought and practice. Each Gharana has its own distinct characteristics, techniques, and repertoire, passed down through generations of musicians.

### Major Gharanas Featured

1. **Gwalior Gharana** (Oldest)
   - Known for its pure and traditional style
   - Founded by Miyan Tansen (1500-1589)
   - Notable for systematic teaching methods and emphasis on voice culture

2. **Kirana Gharana**
   - Famous for its meditative and devotional approach
   - Founded by Abdul Karim Khan and Abdul Wahid Khan
   - Known for its emphasis on alap and slow-tempo development

3. **Jaipur-Atrauli Gharana**
   - Renowned for its complex taans and layakari
   - Founded by Ustad Alladiya Khan
   - Known for its unique approach to rhythm and melody

4. **Patiala Gharana**
   - Famous for its romantic and emotional style
   - Best known through Ustad Bade Ghulam Ali Khan
   - Known for its powerful voice and emotional depth

5. **Agra Gharana**
   - Known for its robust and powerful style
   - Notable for its emphasis on dhrupad and dhamar
   - Famous for its strong rhythmic patterns

6. **Delhi Gharana**
   - Known for its traditional approach
   - Emphasizes the purity of ragas
   - Maintains strong connections to dhrupad style

7. **Bhendi Bazaar Gharana**
   - Known for its unique approach to light classical forms
   - Famous for its thumri and dadra renditions
   - Notable for its influence on film music

8. **Rampur-Sahaswan Gharana**
   - Known for its sophisticated style
   - Combines elements of various gharanas
   - Famous for its intricate taans

9. **Indore Gharana**
   - Founded by Ustad Amir Khan
   - Known for its slow-tempo development
   - Famous for its unique approach to alap

10. **Mewati Gharana**
    - Known for its devotional approach
    - Famous for its unique style of taans
    - Best represented by Pandit Jasraj

11. **Benaras Gharana**
    - Famous for its thumri and light classical forms
    - Known for its emotional depth
    - Best represented by Girija Devi

## Project Features

This project:
1. Reads a curated list of Hindustani Classical vocalists from different gharanas
2. Searches for these artists on Spotify
3. Creates a playlist featuring the top 5 songs of each artist
4. Organizes the playlist to showcase the diversity of Hindustani Classical Music

## Technical Details

The project uses:
- Python with Spotipy for Spotify API integration
- Pandas for data management
- RapidFuzz for fuzzy string matching to handle name variations

## Setup

1. Create a Spotify Developer account and get your credentials
2. Set up your `.env` file with:
   ```
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
   ```
3. Install required packages:
   ```
   pip install spotipy pandas python-dotenv rapidfuzz
   ```
4. Run the script:
   ```
   python main.py
   ```

## Data Source

The project uses a curated CSV file containing information about vocalists from various gharanas, including:
- Gharana name
- Vocalist name
- Period/Era
- Notable contributions

## Contributing

Feel free to contribute by:
1. Adding more artists to the CSV file
2. Improving the search algorithm
3. Adding more features to the playlist generation

## License

This project is open source and available under the MIT License. 
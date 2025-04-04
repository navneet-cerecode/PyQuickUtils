# Instrumentalizer 🎶

**Turn any song into an instrumental track by removing vocals!**

Instrumentalizer is a simple yet powerful Python script that uses [Demucs](https://github.com/facebookresearch/demucs) to extract instrumentals from songs, making it perfect for karaoke or remixing.

## 🚀 Features
- 🎤 Removes vocals from songs
- 🎼 Preserves instrumental quality
- 🔄 Supports multiple audio formats (MP3, WAV, FLAC)

## 📂 Installation
Ensure you have Python installed, then install Demucs:
```bash
pip install demucs
```

## 🎵 Usage
Run the script with an audio file:
```bash
python instrumentalizer.py "path/to/song.mp3"
```

The instrumental version will be saved automatically.

## 🔧 Requirements
- Python 3.7+
- Demucs
- FFmpeg (optional for additional format support)

## 🤝 Contributions
Feel free to contribute by improving the script or adding new features!

## 📜 License
This project is licensed under the MIT License.
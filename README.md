# AudioConverter

Python script to convert `.m4a` files to `.mp3` in bulk.

---

## Usage

1. Run `python convert.py` in the folder with the `.m4a` files you want converted  
2. Wait  
3. Converted `.mp3` files should be there when done

---

## Requires

- [FFmpeg](https://ffmpeg.org/download.html)  
- Pydub: `pip install pydub`

---

## Other file formats

Tested to work with `.webm` also; just replace the extension on lines 5 and 6.

In theory it should also work with any other file type Pydub/FFmpeg allows:

### Example Supported Formats

| Format         | Extensions             | Notes                                      |
|----------------|------------------------|--------------------------------------------|
| **WAV**        | `.wav`                 | Supported natively (no FFmpeg required)    |
| **MP3**        | `.mp3`                 | Requires FFmpeg                            |
| **AAC**        | `.aac`, `.m4a`         | Requires FFmpeg                            |
| **OGG**        | `.ogg`, `.oga`         | Requires FFmpeg                            |
| **FLAC**       | `.flac`                | Requires FFmpeg                            |
| **AIFF**       | `.aiff`, `.aif`        | Requires FFmpeg                            |
| **MP4 Audio**  | `.mp4`, `.m4a`         | Requires FFmpeg                            |
| **WMA**        | `.wma`                 | Requires FFmpeg                            |
| **AMR**        | `.amr`                 | Requires FFmpeg                            |
| **WebM**       | `.webm`                | Requires FFmpeg                            |
| **3GP Audio**  | `.3gp`                 | Requires FFmpeg                            |

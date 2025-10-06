#所有接口统一用 ensure_ascii=False
import json
from flask import Blueprint, current_app
from app.models import Track, Lyric, Playlist
from flask import redirect
bp = Blueprint("api", __name__, url_prefix="/api")

# 统一工具：不转义中文
def json_no_ascii(data):
    return current_app.response_class(
        json.dumps(data, ensure_ascii=False),
        mimetype="application/json; charset=utf-8"
    )

# --------- 心跳 ---------
@bp.get("/")
def index():
    return json_no_ascii({"msg": "iMusic API 运行中"})

# --------- 歌曲 ---------
@bp.get("/tracks")
def list_tracks():
    tracks = Track.query.all()
    return json_no_ascii(
        [{"id": t.id, "name": t.name, "audio_url": t.audio_url} for t in tracks]
    )

@bp.get("/tracks/<int:track_id>")
def get_track(track_id):
    t = Track.query.get_or_404(track_id)
    return json_no_ascii({"id": t.id, "name": t.name, "audio_url": t.audio_url})

# --------- 歌词 ---------
@bp.get("/tracks/<int:track_id>/lyrics")
def get_lyrics(track_id):
    lyric = Lyric.query.filter_by(track_id=track_id).first_or_404()
    return json_no_ascii({"lrc_text": lyric.lrc_text})

# --------- 歌单 ---------
@bp.get("/playlists")
def list_playlists():
    pls = Playlist.query.all()
    return json_no_ascii(
        [{"id": p.id, "name": p.name, "cover_url": p.cover_url} for p in pls]
    )

@bp.get("/playlists/<int:pl_id>")
def get_playlist(pl_id):
    pl = Playlist.query.get_or_404(pl_id)
    tracks = [{"id": t.id, "name": t.name, "audio_url": t.audio_url} for t in pl.tracks]
    return json_no_ascii(
        {"id": pl.id, "name": pl.name, "cover_url": pl.cover_url, "tracks": tracks}
    )


@bp.get("/player")
def player():
    return redirect("/static/player.html")
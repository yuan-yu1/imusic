from app.extensions import db

playlist_track = db.Table(
    'playlist_track',
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id'), primary_key=True),
    db.Column('track_id',    db.Integer, db.ForeignKey('track.id'),    primary_key=True)
)

class Track(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(120), nullable=False)
    audio_url = db.Column(db.String(255), nullable=False)

class Playlist(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(120), nullable=False)
    cover_url = db.Column(db.String(255))
    # 关键：反向关系
    tracks = db.relationship('Track', secondary=playlist_track, backref='playlists')

class Lyric(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), nullable=False)
    lrc_text = db.Column(db.Text, nullable=False)
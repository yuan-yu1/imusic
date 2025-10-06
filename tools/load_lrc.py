import os, glob
from app import create_app, db
from app.models import Track, Lyric

app = create_app()
app.app_context().push()

for lrc_path in glob.glob("static/music/*.lrc"):
    # 去掉后缀拿到歌名
    name_without_ext = os.path.basename(lrc_path)[:-4]
    # 找对应歌曲记录（模糊匹配文件名）
    track = Track.query.filter(Track.name.contains(name_without_ext.replace('-', ''))).first() \
            or Track.query.filter(Track.audio_url.contains(name_without_ext)).first()
    if not track:
        print(f"找不到对应歌曲：{name_without_ext}")
        continue
    # 读 LRC 全文
    with open(lrc_path, encoding='utf-8') as f:
        lrc_text = f.read()
    # 先删后插，避免重复
    Lyric.query.filter_by(track_id=track.id).delete()
    db.session.add(Lyric(track_id=track.id, lrc_text=lrc_text))
    print(f"✔ {os.path.basename(lrc_path)} 已入库 → 歌曲 ID {track.id}")

db.session.commit()
print('全部 LRC 处理完成')
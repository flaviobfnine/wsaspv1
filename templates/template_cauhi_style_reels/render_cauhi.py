# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import glob
import time

project_dir = r"d:\BACKUP_ARQUIVOS\SITES\ASIMOV\SITES\SITE 2\hyperframes-vsl\vsl-preview"
template_dir = r"D:\BACKUP_ARQUIVOS\SITES\ASIMOV\SITES\SITE 2\templates\template_cauhi_style_reels"
sfx_audio = r"D:\BACKUP_ARQUIVOS\SITES\ASIMOV\SITES\SITE 2\templates\sfx\audio_master_reels_sfx.mp3"

# 1. Backup do index.html atual
shutil.copyfile(os.path.join(project_dir, "index.html"), os.path.join(project_dir, "index_vsl_backup.html"))

# 2. Copiar index.html do modelo 2.mp4 para o preview
with open(os.path.join(template_dir, "index.html"), "r", encoding="utf-8") as f:
    template_html = f.read()

with open(os.path.join(project_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(template_html)

# 3. Limpar renders anteriores
for old_f in glob.glob(os.path.join(project_dir, "renders", "vsl-preview_*.mp4")):
    try:
        os.remove(old_f)
    except:
        pass

# 4. Renderizar via HyperFrames
print("Iniciando render do Modelo estilo 2.mp4 (50 segundos)...")
t0 = time.time()
cmd_render = "cmd /c npm run render"
res = subprocess.run(cmd_render, cwd=project_dir, shell=True, capture_output=True, text=True)
t_render = time.time() - t0

if res.returncode != 0:
    print("ERRO no render do template!")
    print(res.stderr[-500:] if res.stderr else res.stdout[-500:])
else:
    print(f"Render visual 9:16 concluído em {t_render:.1f}s")
    
    # 5. Pegar último render e muxar com áudio SFX
    render_files = glob.glob(os.path.join(project_dir, "renders", "vsl-preview_*.mp4"))
    latest_render = max(render_files, key=os.path.getctime)
    
    output_mp4 = os.path.join(template_dir, "reels_modelo_estilo_2mp4.mp4")
    output_public = r"D:\BACKUP_ARQUIVOS\SITES\Mentoria Premier Brand Sports\reels_modelo_estilo_2mp4.mp4"
    
    print("Muxando com áudio e SFX...")
    cmd_mux = f'ffmpeg -y -i "{latest_render}" -i "{sfx_audio}" -c:v copy -c:a aac -b:a 192k -shortest "{output_mp4}"'
    subprocess.run(cmd_mux, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    shutil.copyfile(output_mp4, output_public)
    sz_mb = os.path.getsize(output_public) / (1024 * 1024)
    print(f"VÍDEO REELS ESTILO 2.MP4 PRONTO: {output_public} ({sz_mb:.1f} MB)")

# Restaurar index.html original
shutil.copyfile(os.path.join(project_dir, "index_vsl_backup.html"), os.path.join(project_dir, "index.html"))
print("Ambiente restaurado com sucesso!")

# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import json
import time
import glob

with open("narrative_blocks_enriched.json", "r", encoding="utf-8") as f:
    blocks = json.load(f)

os.makedirs("rendered_parts", exist_ok=True)
os.makedirs("final_parts", exist_ok=True)

print("Iniciando esteira em lote dos 11 blocos da VSL com o novo padrão visual...")

for block in blocks:
    idx = block["index"]
    start = block["start"]
    end = block["end"]
    dur = round(end - start, 2)
    final_part_mp4 = f"final_parts/bloco_{idx:02d}.mp4"
    
    if os.path.exists(final_part_mp4) and os.path.getsize(final_part_mp4) > 1000000:
        print(f"Bloco {idx} já concluído anteriormente. Pulando...")
        continue
    
    print(f"\n==========================================")
    print(f"PROCESSANDO BLOCO {idx}/11: {start}s -> {end}s ({dur}s)")
    print(f"Titulo: {block['title']}")
    print(f"==========================================")
    
    # 1. Copiar index.html do bloco para o index.html raiz
    block_html = f"blocks/block_{idx:02d}/index.html"
    shutil.copyfile(block_html, "index.html")
    
    # 2. Renderizar via HyperFrames
    t0 = time.time()
    cmd_render = "npm.cmd run render"
    print(f"Renderizando vídeo visual via HyperFrames...")
    res = subprocess.run(cmd_render, shell=True, capture_output=True, text=True)
    t_render = time.time() - t0
    
    if res.returncode != 0:
        print(f"ERRO no render do Bloco {idx}!")
        print(res.stderr[-500:] if res.stderr else res.stdout[-500:])
        break
    
    print(f"Render visual do Bloco {idx} concluído em {t_render:.1f}s")
    
    # Encontrar o último arquivo gerado em renders/
    render_files = glob.glob("renders/vsl-preview_*.mp4")
    latest_render = max(render_files, key=os.path.getctime)
    
    # 3. Juntar áudio original do bloco
    audio_file = f"audio_blocks/block_{idx:02d}.mp3"
    print(f"Muxando áudio original ({audio_file})...")
    
    cmd_mux = f'ffmpeg -y -i "{latest_render}" -i "{audio_file}" -c:v copy -c:a aac -b:a 192k -shortest "{final_part_mp4}"'
    subprocess.run(cmd_mux, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    sz_mb = os.path.getsize(final_part_mp4) / (1024 * 1024)
    print(f"BLOCO {idx} FINALIZADO COM SUCESSO: {final_part_mp4} ({sz_mb:.1f} MB)")

# 4. CONCATENAÇÃO FINAL SE TODOS OS 11 BLOCOS ESTIVEREM PRONTOS
all_done = True
for i in range(1, 12):
    f_p = f"final_parts/bloco_{i:02d}.mp4"
    if not os.path.exists(f_p) or os.path.getsize(f_p) < 1000000:
        all_done = False
        print(f"Aviso: Bloco {i} não está pronto para concatenação final.")

if all_done:
    print("\n==========================================")
    print("TODOS OS 11 BLOCOS FINALIZADOS!")
    print("CONCATENANDO VSL COMPLETA DE 12M31S...")
    print("==========================================")
    
    with open("concat_list.txt", "w", encoding="utf-8") as f:
        for i in range(1, 12):
            f.write(f"file 'final_parts/bloco_{i:02d}.mp4'\n")
            
    final_output = r"D:\BACKUP_ARQUIVOS\SITES\Mentoria Premier Brand Sports\vsl_completa_masterclass_premier_brand.mp4"
    cmd_concat = f'ffmpeg -y -f concat -safe 0 -i concat_list.txt -c copy "{final_output}"'
    subprocess.run(cmd_concat, shell=True, check=True)
    
    final_sz = os.path.getsize(final_output) / (1024 * 1024)
    print(f"\n>>> VSL COMPLETA GERADA COM SUCESSO EM: {final_output} ({final_sz:.1f} MB) <<<")
else:
    print("\nEsteira pausada ou incompleta.")

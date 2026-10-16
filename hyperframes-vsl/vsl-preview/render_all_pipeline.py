import os
import shutil
import subprocess
import json
import time

with open("narrative_blocks_enriched.json", "r", encoding="utf-8") as f:
    blocks = json.load(f)

os.makedirs("rendered_parts", exist_ok=True)
os.makedirs("final_parts", exist_ok=True)

print("Iniciando esteira em lote dos 11 blocos da VSL...")

for block in blocks:
    idx = block["index"]
    start = block["start"]
    end = block["end"]
    dur = round(end - start, 2)
    final_part_mp4 = f"final_parts/bloco_{idx:02d}.mp4"
    
    if os.path.exists(final_part_mp4) and os.path.getsize(final_part_mp4) > 1000000:
        print(f"Bloco {idx} ja concluido anteriormente. Pulando...")
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
    print(f"Renderizando video visual via HyperFrames...")
    res = subprocess.run(cmd_render, shell=True, capture_output=True, text=True)
    t_render = time.time() - t0
    
    if res.returncode != 0:
        print(f"ERRO no render do Bloco {idx}!")
        print(res.stderr[-500:] if res.stderr else res.stdout[-500:])
        break
    
    print(f"Render visual do Bloco {idx} concluido em {t_render:.1f}s")
    
    # Encontrar o ultimo arquivo gerado em renders/
    import glob
    render_files = glob.glob("renders/vsl-preview_*.mp4")
    latest_render = max(render_files, key=os.path.getctime)
    
    # 3. Juntar audio original do bloco
    audio_file = f"audio_blocks/block_{idx:02d}.mp3"
    print(f"Muxando audio original ({audio_file})...")
    
    cmd_mux = f'ffmpeg -y -i "{latest_render}" -i "{audio_file}" -c:v copy -c:a aac -b:a 192k -shortest "{final_part_mp4}"'
    subprocess.run(cmd_mux, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    sz_mb = os.path.getsize(final_part_mp4) / (1024 * 1024)
    print(f"BLOCO {idx} FINALIZADO COM SUCESSO: {final_part_mp4} ({sz_mb:.1f} MB)")

print("\n--- TODOS OS BLOCOS DISPONIVEIS PROCESSADOS ---")

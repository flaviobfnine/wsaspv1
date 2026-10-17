# -*- coding: utf-8 -*-
import json
import os

with open("narrative_blocks_enriched.json", "r", encoding="utf-8") as f:
    blocks = json.load(f)

with open("transcripts/transcricao_completa.json", "r", encoding="utf-8") as f:
    full_trans = json.load(f)

all_words = full_trans["words"]

def generate_block_html(block, words_rel):
    b_idx = block["index"]
    b_title = block["title"]
    b_badge = block["badge"]
    b_desc = block["description"]
    bullets = block["bullets"]
    dur = round(block["end"] - block["start"], 2)
    
    # Se bloco <= 5 (até 332.74s = 5m32s), legenda fica sobre o peito (top: 570px)
    # A partir do bloco 6 (após 5m32s), legenda fica na base inferior (bottom: 40px)
    if b_idx <= 5:
        caption_style = """
      #captions-dock {
        position: absolute;
        top: 570px;
        right: 50px;
        width: 1040px;
        display: flex;
        justify-content: center;
        align-items: center;
        pointer-events: none;
        z-index: 15;
      }
        """
    else:
        caption_style = """
      #captions-dock {
        position: absolute;
        bottom: 40px;
        right: 50px;
        width: 1040px;
        display: flex;
        justify-content: center;
        align-items: center;
        pointer-events: none;
        z-index: 15;
      }
        """

    # Divisão dos tempos de cena
    t_s1 = 0.3
    t_s1_end = round(dur * 0.35, 2)
    t_s2 = round(t_s1_end + 0.2, 2)
    t_s2_end = round(dur * 0.68, 2)
    t_s3 = round(t_s2_end + 0.2, 2)

    # Tempos de animação dos cards na Cena 1
    t_c1 = round(dur * 0.05, 2)
    t_a1 = round(dur * 0.12, 2)
    t_c2 = round(dur * 0.15, 2)
    t_a2 = round(dur * 0.22, 2)
    t_c3 = round(dur * 0.25, 2)

    # Tempos de animação dos cards na Cena 2
    t_s2_c1 = round(t_s2 + 1.0, 2)
    t_s2_a = round(t_s2 + (t_s2_end - t_s2) * 0.45, 2)
    t_s2_c2 = round(t_s2 + (t_s2_end - t_s2) * 0.55, 2)

    words_json = json.dumps(words_rel, ensure_ascii=False)

    html_content = f"""<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>VSL Bloco {b_idx} - Premier Brand Sports Masterclass</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Montserrat:wght@600;700;800;900&display=swap"
      rel="stylesheet"
    />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}
      html, body {{
        margin: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        background: #030706;
        font-family: 'Inter', -apple-system, sans-serif;
      }}
      #root {{
        position: relative;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at 20% 30%, #082218 0%, #04140e 45%, #030706 100%);
        overflow: hidden;
      }}

      .ambient-emerald {{
        position: absolute;
        top: -100px;
        left: -100px;
        width: 800px;
        height: 800px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(16, 185, 129, 0.12) 0%, transparent 70%);
        pointer-events: none;
      }}
      .ambient-gold {{
        position: absolute;
        bottom: -150px;
        right: 200px;
        width: 700px;
        height: 700px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(245, 158, 11, 0.08) 0%, transparent 70%);
        pointer-events: none;
      }}

      #header-bar {{
        position: absolute;
        top: 40px;
        left: 50px;
        right: 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 10;
      }}
      .brand-badge {{
        display: flex;
        align-items: center;
        gap: 12px;
      }}
      .brand-dot {{
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #10b981;
        box-shadow: 0 0 12px #10b981;
      }}
      .brand-title {{
        font-family: 'Montserrat', sans-serif;
        font-size: 15px;
        font-weight: 800;
        letter-spacing: 2px;
        color: #fdfbf7;
        text-transform: uppercase;
      }}
      .brand-sub {{
        color: #34d399;
        font-weight: 700;
      }}
      .live-tag {{
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.35);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        color: #34d399;
        text-transform: uppercase;
      }}

      #speaker-frame {{
        position: absolute;
        top: 110px;
        right: 50px;
        width: 1040px;
        height: 820px;
        border-radius: 24px;
        overflow: hidden;
        border: 1px solid rgba(52, 211, 153, 0.25);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), 0 0 30px rgba(16, 185, 129, 0.1);
        background: #04140e;
        z-index: 5;
      }}
      #speaker-video {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: 40% 15%;
        display: block;
      }}
      .speaker-overlay-gradient {{
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(3, 7, 6, 0.05) 0%, rgba(3, 7, 6, 0.4) 100%);
        pointer-events: none;
      }}
      .speaker-name-tag {{
        position: absolute;
        bottom: 24px;
        left: 24px;
        background: rgba(8, 34, 24, 0.85);
        border: 1px solid rgba(52, 211, 153, 0.3);
        padding: 10px 18px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        display: flex;
        flex-direction: column;
      }}
      .tag-name {{
        font-family: 'Montserrat', sans-serif;
        font-size: 15px;
        font-weight: 800;
        color: #fdfbf7;
        letter-spacing: 0.5px;
      }}
      .tag-role {{
        font-size: 12px;
        font-weight: 600;
        color: #34d399;
      }}

      #content-dock {{
        position: absolute;
        top: 110px;
        left: 50px;
        width: 720px;
        height: 820px;
        z-index: 5;
        display: flex;
        flex-direction: column;
        justify-content: center;
      }}
      .scene {{
        position: absolute;
        width: 100%;
        opacity: 0;
        pointer-events: none;
      }}
      .scene.active {{
        opacity: 1;
        pointer-events: auto;
      }}

      .luxury-card {{
        background: rgba(8, 34, 24, 0.65);
        border: 1px solid rgba(52, 211, 153, 0.22);
        border-radius: 20px;
        padding: 34px 38px;
        backdrop-filter: blur(16px);
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        margin-bottom: 20px;
      }}
      .luxury-card-compact {{
        background: rgba(8, 34, 24, 0.7);
        border: 1px solid rgba(52, 211, 153, 0.25);
        border-radius: 18px;
        padding: 22px 28px;
        backdrop-filter: blur(14px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        margin-bottom: 20px;
      }}
      .card-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
      }}
      .card-badge {{
        background: rgba(16, 185, 129, 0.18);
        border: 1px solid #10b981;
        color: #6ee7b7;
        font-family: 'Montserrat', sans-serif;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        padding: 5px 12px;
        border-radius: 20px;
        display: inline-block;
      }}
      .luxury-card-title {{
        font-family: 'Montserrat', sans-serif;
        font-size: 26px;
        font-weight: 900;
        color: #fdfbf7;
        text-transform: uppercase;
        margin-bottom: 8px;
        line-height: 1.25;
      }}
      .luxury-card-title-sm {{
        font-family: 'Montserrat', sans-serif;
        font-size: 22px;
        font-weight: 800;
        color: #fdfbf7;
        text-transform: uppercase;
        margin-top: 8px;
        line-height: 1.25;
      }}
      .luxury-card-desc {{
        font-family: 'Inter', sans-serif;
        font-size: 17px;
        font-weight: 500;
        color: #e2e8f0;
        line-height: 1.5;
      }}

      /* ESTILIZAÇÃO DOS CARDS QUADRADOS COM FLUXO E SETAS */
      .flow-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        margin-top: 8px;
        width: 100%;
      }}
      .two-cols {{
        gap: 16px;
      }}
      .square-card {{
        flex: 1;
        min-height: 195px;
        background: rgba(8, 34, 24, 0.8);
        border: 1px solid rgba(52, 211, 153, 0.3);
        border-radius: 18px;
        padding: 22px 18px;
        backdrop-filter: blur(16px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
      }}
      .square-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #10b981, #34d399);
      }}
      .square-card.alert {{
        border-color: rgba(239, 68, 68, 0.4);
      }}
      .square-card.alert::before {{
        background: linear-gradient(90deg, #f59e0b, #ef4444);
      }}
      .square-card.gold-card {{
        border-color: rgba(245, 158, 11, 0.45);
        background: rgba(18, 30, 20, 0.85);
      }}
      .square-card.gold-card::before {{
        background: linear-gradient(90deg, #f59e0b, #fbbf24);
      }}
      .card-tag {{
        font-family: 'Montserrat', sans-serif;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #34d399;
      }}
      .card-tag.alert, .card-tag.red {{
        color: #f87171;
      }}
      .card-tag.gold {{
        color: #fbbf24;
      }}
      .square-title {{
        font-family: 'Montserrat', sans-serif;
        font-size: 19px;
        font-weight: 800;
        color: #fdfbf7;
        margin: 6px 0;
        line-height: 1.2;
      }}
      .square-desc {{
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        font-weight: 500;
        color: #cbd5e1;
        line-height: 1.4;
      }}
      .flow-arrow {{
        color: #34d399;
        font-size: 26px;
        font-weight: 900;
        opacity: 0.8;
        text-shadow: 0 0 12px rgba(52, 211, 153, 0.6);
        display: flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        flex-shrink: 0;
      }}

      {caption_style}

      .caption-pill {{
        background: rgba(8, 34, 24, 0.94);
        border: 1px solid rgba(52, 211, 153, 0.3);
        padding: 12px 30px;
        border-radius: 18px;
        backdrop-filter: blur(14px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8), 0 0 25px rgba(16, 185, 129, 0.15);
        display: flex;
        gap: 12px;
        align-items: center;
      }}
      .cap-text {{
        font-family: 'Inter', sans-serif;
        font-size: 28px;
        font-weight: 700;
        color: #e2e8f0;
        letter-spacing: -0.2px;
      }}
      .cap-w {{
        display: inline-block;
        margin: 0 6px;
        color: #94a3b8;
      }}
      .cap-w.active {{
        color: #fbbf24;
        font-weight: 800;
        text-shadow: 0 0 12px rgba(251, 191, 36, 0.6);
      }}
    </style>
  </head>
  <body>
    <div
      id="root"
      data-composition-id="main"
      data-start="0"
      data-width="1920"
      data-height="1080"
      data-duration="{dur}"
    >
      <div class="ambient-emerald"></div>
      <div class="ambient-gold"></div>

      <div id="header-bar">
        <div class="brand-badge">
          <div class="brand-dot"></div>
          <div class="brand-title">PREMIER BRAND SPORTS <span class="brand-sub">| MENTORIA VIP</span></div>
        </div>
        <div class="live-tag">MÉTODO EXCLUSIVO DE CONVERSÃO</div>
      </div>

      <div id="speaker-frame">
        <video
          id="speaker-video"
          src="assets/video_blocks/block_{b_idx:02d}.mp4"
          data-start="0"
          data-duration="{dur}"
          muted
          playsinline
          preload="auto"
        ></video>
        <div class="speaker-overlay-gradient"></div>
        <div class="speaker-name-tag">
          <span class="tag-name">FLÁVIO BFNINE</span>
          <span class="tag-role">Fundador e Mentor da Premier Brand Sports</span>
        </div>
      </div>

      <div id="content-dock">
        <!-- CENA 1: FLUXO DE 3 CARDS QUADRADOS (0 a 35%) -->
        <div id="scene-1" class="scene active">
          <div class="luxury-card-compact">
            <span class="card-badge">{b_badge}</span>
            <div class="luxury-card-title-sm">{b_title}</div>
          </div>

          <div class="flow-container">
            <div class="square-card flow-c1">
              <div class="card-tag">01. IDENTIFICAÇÃO</div>
              <div class="square-title">{bullets[0]['label']}</div>
              <div class="square-desc">{bullets[0]['detail']}</div>
            </div>
            <div class="flow-arrow flow-a1">→</div>
            <div class="square-card flow-c2">
              <div class="card-tag">02. IMPACTO</div>
              <div class="square-title">{bullets[1]['label']}</div>
              <div class="square-desc">{bullets[1]['detail']}</div>
            </div>
            <div class="flow-arrow flow-a2">→</div>
            <div class="square-card flow-c3 gold-card">
              <div class="card-tag gold">03. RESULTADO</div>
              <div class="square-title">{bullets[2]['label']}</div>
              <div class="square-desc">{bullets[2]['detail']}</div>
            </div>
          </div>
        </div>

        <!-- CENA 2: COMPARATIVO EM CARDS QUADRADOS (35% a 68%) -->
        <div id="scene-2" class="scene">
          <div class="luxury-card-compact">
            <span class="card-badge">DIRETRIZ ESTRATÉGICA</span>
            <div class="luxury-card-title-sm">{bullets[1]['label']}</div>
          </div>

          <div class="flow-container two-cols">
            <div class="square-card alert flow-sc2-c1">
              <div class="card-tag alert">O ERRO COMUM</div>
              <div class="square-title">Padrão do Mercado</div>
              <div class="square-desc">{bullets[0]['detail']}</div>
            </div>
            <div class="flow-arrow flow-sc2-a">→</div>
            <div class="square-card gold-card flow-sc2-c2">
              <div class="card-tag gold">O PADRÃO PREMIER</div>
              <div class="square-title">Método Blindado</div>
              <div class="square-desc">{bullets[2]['detail']}</div>
            </div>
          </div>
        </div>

        <!-- CENA 3: SÍNTESE E VISÃO EMPRESARIAL (68% a 100%) -->
        <div id="scene-3" class="scene">
          <div class="luxury-card">
            <div class="card-header">
              <span class="card-badge">VISÃO DO FUNDADOR</span>
            </div>
            <div class="luxury-card-title">{bullets[2]['label']}</div>
            <div class="luxury-card-desc">{b_desc}</div>
          </div>
        </div>
      </div>

      <div id="captions-dock">
        <div class="caption-pill">
          <div id="caption-box" class="cap-text"></div>
        </div>
      </div>
    </div>

    <script>
      const tl = gsap.timeline({{ paused: true }});

      tl.fromTo(
        "#speaker-frame",
        {{ opacity: 0, scale: 0.9, y: 30 }},
        {{ opacity: 1, scale: 1, y: 0, duration: 0.8, ease: "power3.out" }},
        0.0
      );

      // TRANSIÇÃO DE CENAS E ANIMAÇÃO DOS CARDS
      // CENA 1
      tl.fromTo("#scene-1", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, {t_s1});
      tl.fromTo(".flow-c1", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, {t_c1});
      tl.fromTo(".flow-a1", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, {t_a1});
      tl.fromTo(".flow-c2", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, {t_c2});
      tl.fromTo(".flow-a2", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, {t_a2});
      tl.fromTo(".flow-c3", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, {t_c3});
      tl.to("#scene-1", {{ opacity: 0, x: 20, duration: 0.3, ease: "power2.in" }}, {t_s1_end});

      // CENA 2
      tl.fromTo("#scene-2", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, {t_s2});
      tl.fromTo(".flow-sc2-c1", {{ opacity: 0, scale: 0.88, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, {t_s2_c1});
      tl.fromTo(".flow-sc2-a", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3 }}, {t_s2_a});
      tl.fromTo(".flow-sc2-c2", {{ opacity: 0, scale: 0.88, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, {t_s2_c2});
      tl.to("#scene-2", {{ opacity: 0, x: 20, duration: 0.3, ease: "power2.in" }}, {t_s2_end});

      // CENA 3
      tl.fromTo("#scene-3", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, {t_s3});

      // LEGENDAS DETERMINÍSTICAS (PALAVRA POR PALAVRA)
      const words = {words_json};

      {{
        const captionBox = document.getElementById("caption-box");
        const CHUNK_SIZE = 4;
        for (let i = 0; i < words.length; i += CHUNK_SIZE) {{
          const chunk = words.slice(i, i + CHUNK_SIZE);
          const tStart = chunk[0].s;
          const tEnd = chunk[chunk.length - 1].e + 0.15;

          const chunkEl = document.createElement("span");
          chunkEl.style.display = "none";
          chunkEl.id = `chunk-${{i}}`;

          chunk.forEach((w, wIdx) => {{
            const span = document.createElement("span");
            span.className = "cap-w";
            span.id = `w-${{i + wIdx}}`;
            span.textContent = w.t;
            chunkEl.appendChild(span);
          }});

          captionBox.appendChild(chunkEl);

          tl.set(chunkEl, {{ display: "inline-block" }}, tStart);
          chunk.forEach((w, wIdx) => {{
            tl.set(`#w-${{i + wIdx}}`, {{ className: "cap-w active" }}, w.s);
            tl.set(`#w-${{i + wIdx}}`, {{ className: "cap-w" }}, w.e);
          }});
          tl.set(chunkEl, {{ display: "none" }}, tEnd);
        }}
      }}

      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""
    return html_content

# Gerar HTML para os blocos 2 a 11 (o bloco 1 já foi feito e validado com precisão manual)
for block in blocks:
    idx = block["index"]
    if idx == 1:
        print("Bloco 1 já configurado com rigor manual. Mantido!")
        continue
    
    start = block["start"]
    end = block["end"]
    
    b_words = []
    for w in all_words:
        if w["s"] >= start and w["s"] < end:
            b_words.append({
                "t": w["t"],
                "s": round(w["s"] - start, 2),
                "e": round(w["e"] - start, 2)
            })
            
    html_str = generate_block_html(block, b_words)
    with open(f"blocks/block_{idx:02d}/index.html", "w", encoding="utf-8") as f:
        f.write(html_str)

print("Todos os blocos de 02 a 11 atualizados com sucesso com o novo padrão!")

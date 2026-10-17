# -*- coding: utf-8 -*-
import json

# Carregar transcrição completa
trans = json.load(open('transcripts/transcricao_completa.json', encoding='utf-8'))
all_words = trans['words']

start_b2 = 65.76
end_b2 = 131.78
dur_b2 = round(end_b2 - start_b2, 2)

words_b2 = []
for w in all_words:
    if w["s"] >= start_b2 and w["s"] < end_b2:
        words_b2.append({
            "t": w["t"],
            "s": round(w["s"] - start_b2, 2),
            "e": round(w["e"] - start_b2, 2)
        })

words_json_b2 = json.dumps(words_b2, ensure_ascii=False)

html_b2 = f"""<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>VSL Bloco 2 - Premier Brand Sports Masterclass</title>
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

      .luxury-card-compact {{
        background: rgba(8, 34, 24, 0.7);
        border: 1px solid rgba(52, 211, 153, 0.25);
        border-radius: 18px;
        padding: 22px 28px;
        backdrop-filter: blur(14px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        margin-bottom: 20px;
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
      .luxury-card-title-sm {{
        font-family: 'Montserrat', sans-serif;
        font-size: 22px;
        font-weight: 800;
        color: #fdfbf7;
        text-transform: uppercase;
        margin-top: 8px;
        line-height: 1.25;
      }}

      .flow-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        margin-top: 8px;
        width: 100%;
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
      .card-tag.alert {{
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

      /* LEGENDA REBAIXADA (top: 570px) PARA COBRIR BOTÃO DA CAMISA */
      #captions-dock {{
        position: absolute;
        top: 570px;
        right: 50px;
        width: 1040px;
        display: flex;
        justify-content: center;
        align-items: center;
        pointer-events: none;
        z-index: 15;
      }}
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
      data-duration="{dur_b2}"
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
          src="assets/video_blocks/block_02.mp4"
          data-start="0"
          data-duration="{dur_b2}"
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
        <!-- CENA 1: FILTRO DE QUALIFICAÇÃO (0s a 15.8s) -->
        <div id="scene-1" class="scene active">
          <div class="luxury-card-compact">
            <span class="card-badge">FILTRO DE QUALIFICAÇÃO</span>
            <div class="luxury-card-title-sm">Para Quem é Este Vídeo</div>
          </div>

          <div class="flow-container">
            <div class="square-card flow-c1">
              <div class="card-tag">01. NÃO É ATALHO</div>
              <div class="square-title">Sem Mágica</div>
              <div class="square-desc">Não existe botão mágico para construir marca esportiva</div>
            </div>
            <div class="flow-arrow flow-a1">→</div>
            <div class="square-card flow-c2">
              <div class="card-tag">02. CONFECCIONISTA</div>
              <div class="square-title">Fábrica Real</div>
              <div class="square-desc">Para quem já produz e fatura, mas quer virar referência</div>
            </div>
            <div class="flow-arrow flow-a2">→</div>
            <div class="square-card flow-c3 gold-card">
              <div class="card-tag gold">03. POSICIONAMENTO</div>
              <div class="square-title">Referência Local</div>
              <div class="square-desc">O mecanismo prático validado no chão da BF9</div>
            </div>
          </div>
        </div>

        <!-- CENA 2: O CAOS DO CHÃO DE FÁBRICA (16.0s a 43.5s - SINCRONIZADO NO MILISSEGUNDO DA FALA) -->
        <div id="scene-2" class="scene">
          <div class="luxury-card-compact">
            <span class="card-badge">A VERDADE DO CHÃO DE FÁBRICA</span>
            <div class="luxury-card-title-sm">Onde Seu Lucro Está Vazando</div>
          </div>

          <div class="flow-container">
            <div class="square-card alert flow-s2-c1">
              <div class="card-tag alert">01. MESA DE CORTE</div>
              <div class="square-title">Peça Errada</div>
              <div class="square-desc">Tecido acumulado no chão virando prejuízo na bancada</div>
            </div>
            <div class="flow-arrow flow-s2-a1">→</div>
            <div class="square-card alert flow-s2-c2">
              <div class="card-tag alert">02. IMPRESSÃO</div>
              <div class="square-title">Perfil Errado</div>
              <div class="square-desc">Soltando um montão de impressão opaca sem vida</div>
            </div>
            <div class="flow-arrow flow-s2-a2">→</div>
            <div class="square-card alert flow-s2-c3">
              <div class="card-tag alert">03. PRENSA TÉRMICA</div>
              <div class="square-title">Prensa & Estria</div>
              <div class="square-desc">Um lado preto, outro opaco. Pagando do bolso pra refazer</div>
            </div>
          </div>
        </div>

        <!-- CENA 3: A ESCRAVIDÃO OPERACIONAL (43.8s a 66.02s) -->
        <div id="scene-3" class="scene">
          <div class="luxury-card-compact">
            <span class="card-badge">O GARGALO DA ROTINA</span>
            <div class="luxury-card-title-sm">Você Refém da Operação</div>
          </div>

          <div class="flow-container">
            <div class="square-card alert flow-s3-c1">
              <div class="card-tag alert">01. COSTURA</div>
              <div class="square-title">Sem Padrão</div>
              <div class="square-desc">Costureira perdida perguntando pra você como faz</div>
            </div>
            <div class="flow-arrow flow-s3-a1">→</div>
            <div class="square-card flow-s3-c2">
              <div class="card-tag">02. NOTURNO</div>
              <div class="square-title">8h da Noite</div>
              <div class="square-desc">Quem tá na impressora e na prensa sublimando?</div>
            </div>
            <div class="flow-arrow flow-s3-a2">→</div>
            <div class="square-card gold-card flow-s3-c3">
              <div class="card-tag gold">03. O OPERÁRIO</div>
              <div class="square-title">Você Sozinho</div>
              <div class="square-desc">Dobrando camiseta até a madrugada para entrega de amanhã</div>
            </div>
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

      // ==========================================
      // SINCRONIZAÇÃO CIRÚRGICA DOS CARDS COM A FALA
      // ==========================================
      
      // CENA 1: 0.0s a 15.8s
      tl.fromTo("#scene-1", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, 0.2);
      // Card 1: 0.8s ("isso aqui não é pra você")
      tl.fromTo(".flow-c1", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 0.8);
      tl.fromTo(".flow-a1", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 2.5);
      // Card 2: 2.8s ("se você quiser que sua confecção esportiva seja referência")
      tl.fromTo(".flow-c2", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 2.8);
      tl.fromTo(".flow-a2", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 7.2);
      // Card 3: 7.6s ("mecanismo que eu uso aqui hoje na BF9")
      tl.fromTo(".flow-c3", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 7.6);
      tl.to("#scene-1", {{ opacity: 0, x: 20, duration: 0.3, ease: "power2.in" }}, 15.6);

      // CENA 2: 15.9s a 43.5s (Minuto 1:18 até 1:49)
      // Flávio fala aos 15.9s: "Vamos falar a verdade aqui..."
      tl.fromTo("#scene-2", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, 15.9);
      // Card 1: 17.0s (EXATAMENTE quando fala "você chega de manhã... peça errada... tecido acumulado no chão")
      tl.fromTo(".flow-s2-c1", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 17.0);
      // Seta 1: 27.5s
      tl.fromTo(".flow-s2-a1", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 27.5);
      // Card 2: 28.0s (EXATAMENTE quando fala "o perfil de cor configurado errado soltando impressão opaca")
      tl.fromTo(".flow-s2-c2", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 28.0);
      // Seta 2: 32.0s
      tl.fromTo(".flow-s2-a2", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 32.0);
      // Card 3: 32.3s (EXATAMENTE quando fala "a prensa está fazendo estria... um lado preto outro opaco")
      tl.fromTo(".flow-s2-c3", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 32.3);
      tl.to("#scene-2", {{ opacity: 0, x: 20, duration: 0.3, ease: "power2.in" }}, 43.5);

      // CENA 3: 43.8s a 66.02s
      tl.fromTo("#scene-3", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, 43.8);
      // Card 1: 44.0s (EXATAMENTE quando fala "Lá na costura ordem de produção sem padrão... costureira perdida")
      tl.fromTo(".flow-s3-c1", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 44.0);
      // Seta 1: 52.5s
      tl.fromTo(".flow-s3-a1", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 52.5);
      // Card 2: 53.0s (EXATAMENTE quando fala "E quando dá 8 horas da noite quem que tá na impressora... na prensa?")
      tl.fromTo(".flow-s3-c2", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 53.0);
      // Seta 2: 62.0s
      tl.fromTo(".flow-s3-a2", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 62.0);
      // Card 3: 63.5s (EXATAMENTE quando fala "dobrando camiseta pra entrega amanhã? Você.")
      tl.fromTo(".flow-s3-c3", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 63.5);

      // LEGENDAS DETERMINÍSTICAS (PALAVRA POR PALAVRA)
      const words = {words_json_b2};

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

with open('blocks/block_02/index.html', 'w', encoding='utf-8') as f:
    f.write(html_b2)

print("Bloco 02 atualizado com sincronização cirúrgica na fala!")

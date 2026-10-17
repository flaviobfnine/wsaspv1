# -*- coding: utf-8 -*-
import json

# Carregar transcrição completa
trans = json.load(open('transcripts/transcricao_completa.json', encoding='utf-8'))
all_words = trans['words']

start_b3 = 131.78
end_b3 = 199.58
dur_b3 = round(end_b3 - start_b3, 2)

words_b3 = []
for w in all_words:
    if w["s"] >= start_b3 and w["s"] < end_b3:
        words_b3.append({
            "t": w["t"],
            "s": round(w["s"] - start_b3, 2),
            "e": round(w["e"] - start_b3, 2)
        })

words_json_b3 = json.dumps(words_b3, ensure_ascii=False)

html_b3 = f"""<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>VSL Bloco 3 - Premier Brand Sports Masterclass</title>
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
      data-duration="{dur_b3}"
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
          src="assets/video_blocks/block_03.mp4"
          data-start="0"
          data-duration="{dur_b3}"
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
        <!-- CENA 1: OS TIRADORES DE PEDIDO (0s a 18.2s - 2:12 a 2:30 de vídeo) -->
        <div id="scene-1" class="scene active">
          <div class="luxury-card-compact">
            <span class="card-badge">O FALSO COMERCIAL</span>
            <div class="luxury-card-title-sm">Tiradores de Pedido vs Vendedores</div>
          </div>

          <div class="flow-container">
            <div class="square-card alert flow-c1">
              <div class="card-tag alert">01. O COMERCIAL</div>
              <div class="square-title">Tiradores de Pedido</div>
              <div class="square-desc">Eles só vendem porque você entrega as vendas para eles</div>
            </div>
            <div class="flow-arrow flow-a1">→</div>
            <div class="square-card alert flow-c2">
              <div class="card-tag alert">02. REFÉM DE TIMINHO</div>
              <div class="square-title">Guerra de R$ 2</div>
              <div class="square-desc">Pedem desconto de R$ 2, prazo de 10 dias e ameaçam com vizinho</div>
            </div>
            <div class="flow-arrow flow-a2">→</div>
            <div class="square-card alert flow-c3">
              <div class="card-tag alert">03. MARGEM ZERO</div>
              <div class="square-title">O Dono Sangra</div>
              <div class="square-desc">O concorrente da esquina ditando o preço da sua confecção</div>
            </div>
          </div>
        </div>

        <!-- CENA 2: AS DUAS FALSAS SOLUÇÕES (18.5s a 39.0s - 2:30 a 2:50 de vídeo - SINCRONIZADO NO ATO DA FALA) -->
        <div id="scene-2" class="scene">
          <div class="luxury-card-compact">
            <span class="card-badge">O MAIOR VENENO NESSA HORA</span>
            <div class="luxury-card-title-sm">Tentando Tapar o Sol com a Peneira</div>
          </div>

          <div class="flow-container two-cols">
            <div class="square-card alert flow-sc2-c1">
              <div class="card-tag alert">ILUSÃO 01 (R$ 90 MIL)</div>
              <div class="square-title">Máquina Mais Rápida</div>
              <div class="square-desc">Achar que comprar impressora de 90 mil reais resolve erro de gestão</div>
            </div>
            <div class="flow-arrow flow-sc2-a">→</div>
            <div class="square-card alert flow-sc2-c2">
              <div class="card-tag alert">ILUSÃO 02 (MARKETING)</div>
              <div class="square-title">Agência de Fora</div>
              <div class="square-desc">Contratar agência para post bonitinho sem entender o mercado</div>
            </div>
          </div>
        </div>

        <!-- CENA 3: A REALIDADE CRUCIAL (39.2s a 67.8s) -->
        <div id="scene-3" class="scene">
          <div class="luxury-card-compact">
            <span class="card-badge">O DIAGNÓSTICO REAL</span>
            <div class="luxury-card-title-sm">Perdendo Dinheiro Mais Rápido</div>
          </div>

          <div class="flow-container">
            <div class="square-card alert flow-s3-c1">
              <div class="card-tag alert">01. PREJUÍZO ACELERADO</div>
              <div class="square-title">Sem Processo</div>
              <div class="square-desc">Máquina rápida com mesa desregulada só faz queimar dinheiro mais rápido</div>
            </div>
            <div class="flow-arrow flow-s3-a1">→</div>
            <div class="square-card alert flow-s3-c2">
              <div class="card-tag alert">02. AGÊNCIA SEM NICHO</div>
              <div class="square-title">Banco de Imagem</div>
              <div class="square-desc">Não sabem o que é sublimação nem poliéster. Post que você mesmo faz</div>
            </div>
            <div class="flow-arrow flow-s3-a2">→</div>
            <div class="square-card alert flow-s3-c3">
              <div class="card-tag alert">03. CUSTO FIXO INÚTIL</div>
              <div class="square-title">Mensalidade Cara</div>
              <div class="square-desc">Mais um boleto que não devolve um real em vendas reais</div>
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

      // CENA 1: 0.0s a 18.2s
      tl.fromTo("#scene-1", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, 0.2);
      // Card 1: 0.5s ("E lá no comercial os tiradores de pedido...")
      tl.fromTo(".flow-c1", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 0.5);
      tl.fromTo(".flow-a1", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 7.2);
      // Card 2: 7.7s ("Você ainda fica refém de timinho que fica pedindo desconto de 2 reais...")
      tl.fromTo(".flow-c2", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 7.7);
      tl.fromTo(".flow-a2", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 11.5);
      // Card 3: 11.8s ("Pede prazo de 10 dias e ainda fica te ameaçando falando que o concorrente da esquina é mais barato")
      tl.fromTo(".flow-c3", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 11.8);
      tl.to("#scene-1", {{ opacity: 0, x: 20, duration: 0.3, ease: "power2.in" }}, 18.2);

      // CENA 2: 18.5s a 39.0s (Minuto 2:30 a 2:50 de vídeo)
      // Flávio fala aos 18.6s: "E sabe qual que é o maior veneno nessa hora? É a ilusão..."
      tl.fromTo("#scene-2", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, 18.5);
      // Card 1: 25.0s (EXATAMENTE quando fala "Eu acho que eu preciso comprar aquela impressora mais rápida que custa 90 mil reais")
      tl.fromTo(".flow-sc2-c1", {{ opacity: 0, scale: 0.88, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 25.0);
      tl.fromTo(".flow-sc2-a", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3 }}, 31.0);
      // Card 2: 31.5s (EXATAMENTE quando fala "Ou pior ainda, vai achar que precisa contratar uma agência de marketing pra post bonitinho")
      tl.fromTo(".flow-sc2-c2", {{ opacity: 0, scale: 0.88, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 31.5);
      tl.to("#scene-2", {{ opacity: 0, x: 20, duration: 0.3, ease: "power2.in" }}, 39.0);

      // CENA 3: 39.2s a 67.8s
      // Flávio fala aos 39.5s: "Mas pare e pensa comigo, se você está perdendo dinheiro na mesa de corte..."
      tl.fromTo("#scene-3", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, 39.2);
      // Card 1: 40.0s (EXATAMENTE quando fala "comprar máquina mais rápida só vai fazer você perder dinheiro mais rápido")
      tl.fromTo(".flow-s3-c1", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 40.0);
      tl.fromTo(".flow-s3-a1", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 52.0);
      // Card 2: 52.8s (EXATAMENTE quando fala "E a agência? Os caras não sabem nem o que é sublimação nem poliéster... banco de imagem")
      tl.fromTo(".flow-s3-c2", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 52.8);
      tl.fromTo(".flow-s3-a2", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, 62.0);
      // Card 3: 63.8s (EXATAMENTE quando fala "outro custo que você vai ter com a mensalidade daquela agência")
      tl.fromTo(".flow-s3-c3", {{ opacity: 0, scale: 0.85, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.4)" }}, 63.8);

      // LEGENDAS DETERMINÍSTICAS (PALAVRA POR PALAVRA)
      const words = {words_json_b3};

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

with open('blocks/block_03/index.html', 'w', encoding='utf-8') as f:
    f.write(html_b3)

print("Bloco 03 atualizado com sincronização cirúrgica na fala!")

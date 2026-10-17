import re

with open('blocks/block_01/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Enquadramento da camisa inteira no cabide:
c = c.replace('width: 900px;\n        height: 820px;', 'width: 1040px;\n        height: 820px;')
c = c.replace('object-position: center 20%;', 'object-position: 40% 15%;')
c = c.replace('width: 820px;\n        height: 820px;', 'width: 720px;\n        height: 820px;')
c = c.replace('right: 60px;', 'right: 50px;')
c = c.replace('left: 60px;\n        right: 60px;', 'left: 50px;\n        right: 50px;')
c = c.replace('left: 60px;', 'left: 50px;')

# 2. Corrigir nome e cargo do Flavio:
c = c.replace('FLÁVIO SILVA', 'FLÁVIO BFNINE')
c = c.replace('Fundador BFNINE & Mentor Premier Brand', 'Fundador e Mentor da Premier Brand Sports')

# 3. Remover os nomes amarelos do topo dos cards (<span class="card-step">...</span>):
c = re.sub(r'<span class="card-step">.*?</span>', '', c)

# 4. Posicionar a legenda exatamente sobre o botao aberto no meio do peito:
old_dock = """      #captions-dock {
        position: absolute;
        bottom: 90px;
        left: 0;
        right: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        pointer-events: none;
        z-index: 10;
      }"""

new_dock = """      #captions-dock {
        position: absolute;
        top: 510px;
        right: 50px;
        width: 1040px;
        display: flex;
        justify-content: center;
        align-items: center;
        pointer-events: none;
        z-index: 15;
      }"""

c = c.replace(old_dock, new_dock)

with open('blocks/block_01/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Ajustes do Minuto 1 aplicados no index.html com sucesso!")

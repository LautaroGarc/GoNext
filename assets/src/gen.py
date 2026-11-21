#!/usr/bin/env python3
"""Genera los SVG del README de GoNext.

Uso (desde la raíz del repo):

    python3 assets/src/gen.py

Escribe en assets/ ocho archivos: banner y ciclo de vida, en variante
oscura/clara y ancha (960px) / angosta (480px, para pantallas chicas).

Todo se dibuja sobre una grilla de celdas de 10x22 px. La tipografía es
Martian Mono (OFL, ver fonts/OFL.txt), instanciada en wght 400/700 y wdth 100
y recortada a ASCII + acentos del español con fontTools; los .woff2 se
embeben en cada SVG para que GitHub los muestre igual en cualquier equipo.
"""
import base64
import os
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..'))

CW, RH = 10, 22          # celda: 10px de ancho, 22px de alto
FS = CW / 0.7            # Martian Mono avanza 0.7em → 10px por carácter


def b64(name):
    with open(os.path.join(HERE, 'fonts', name), 'rb') as f:
        return base64.b64encode(f.read()).decode()


FONT_CSS = (
    "@font-face{font-family:GN;font-weight:400;src:url(data:font/woff2;base64,%s) format('woff2')}"
    "@font-face{font-family:GN;font-weight:700;src:url(data:font/woff2;base64,%s) format('woff2')}"
) % (b64('MartianMono-Regular.subset.woff2'), b64('MartianMono-Bold.subset.woff2'))

# El cian es de Go: comandos, métodos HTTP, rutas y la mitad GO del wordmark.
# El ámbar marca estado. El resto es tinta y gris de comentario.
THEMES = {
    'dark':  dict(bg='#16181d', edge='#2b2f37', seam='#2a2e35', ink='#e6e1d6', dim='#868e9b',
                  cyan='#00add8', amber='#e0a84f', cell='#1e2127'),
    'light': dict(bg='#f6f4ef', edge='#d9d4c8', seam='#e0dbd0', ink='#1d2026', dim='#5b6270',
                  cyan='#006f91', amber='#8a560a', cell='#ebe7de'),
}


def x(col):
    return col * CW


def base(row):
    return row * RH + 15   # línea base dentro de la fila


def text(col, row, segs, cls=''):
    """Una línea de texto hecha de segmentos (texto, rol[, 'b'])."""
    parts = []
    for seg in segs:
        txt, role = seg[0], seg[1]
        weight = ' font-weight="700"' if len(seg) > 2 and seg[2] == 'b' else ''
        parts.append(f'<tspan class="{role}"{weight}>{escape(txt)}</tspan>')
    c = f' class="{cls}"' if cls else ''
    return f'<text x="{x(col)}" y="{base(row):g}"{c}>{"".join(parts)}</text>'


def seam_h(y, w):
    return f'<path class="seam" d="M1 {y:g}H{w-1}"/>'


def seam_v(xx, y0, y1):
    return f'<path class="seam" d="M{xx:g} {y0:g}V{y1:g}"/>'


def doc(w, h, theme, body, label, extra_css=''):
    c = THEMES[theme]
    css = (FONT_CSS +
           f"text{{font-family:GN,ui-monospace,Menlo,Consolas,monospace;font-size:{FS:.4f}px;fill:{c['ink']};white-space:pre}}"
           f".ink{{fill:{c['ink']}}}.dim{{fill:{c['dim']}}}.cyan{{fill:{c['cyan']}}}.amber{{fill:{c['amber']}}}"
           f".px{{fill:{c['ink']}}}.px.go{{fill:{c['cyan']}}}.ghost{{fill:{c['cell']}}}"
           f".seam{{stroke:{c['seam']};stroke-width:1;fill:none}}.wire{{stroke:{c['dim']};stroke-width:1;fill:none}}"
           f".axis{{stroke:{c['dim']};stroke-width:2}}"
           f".node{{fill:{c['bg']};stroke:{c['ink']};stroke-width:2}}.node.own{{fill:{c['ink']}}}"
           f".node.later{{stroke:{c['dim']};stroke-dasharray:2 2}}"
           f".err{{stroke:{c['amber']};stroke-width:1.5;fill:none;stroke-dasharray:3 3}}"
           + extra_css)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(label)}">'
            f'<style>{css}</style>'
            f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" fill="{c["bg"]}" stroke="{c["edge"]}"/>'
            + body + '</svg>')


# ---------------------------------------------------------------- banner
GLYPHS = {
    'G': [".###.", "#...#", "#....", "#.###", "#...#", "#...#", ".###."],
    'O': [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    'N': ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"],
    'E': ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    'X': ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    'T': ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
}


def wordmark(col0, row0, pw, ph, gap):
    """GONEXT con celdas sólidas. Cada píxel mide pw columnas x ph filas."""
    out = []
    w, h = pw * CW, ph * RH
    for i, ch in enumerate("GONEXT"):
        gx = col0 + i * (5 * pw + gap)
        for r, line in enumerate(GLYPHS[ch]):
            for k, bit in enumerate(line):
                px, py = x(gx + k * pw) + 1, row0 * RH + r * h + 1
                if bit == '#':
                    cls = 'px go' if ch in 'GO' else 'px'
                    delay = 1.05 + r * 0.045 + i * 0.03
                    out.append(f'<rect class="{cls} cellin" x="{px:g}" y="{py:g}" width="{w-2:g}" '
                               f'height="{h-2:g}" style="animation-delay:{delay:.3f}s"/>')
                else:
                    out.append(f'<rect class="ghost" x="{px:g}" y="{py:g}" width="{w-2:g}" height="{h-2:g}"/>')
    return ''.join(out)


TREE = [  # (profundidad, nombre)
    (0, 'api/'),
    (1, 'app.module.go'),
    (1, 'go.mod'),
    (1, 'main.go'),
    (1, 'users/'),
    (2, 'users.module.go'),
    (2, 'users.controller.go'),
    (2, 'users.service.go'),
]


def tree(col, row):
    """Árbol de archivos con uniones dibujadas, no caracteres."""
    out = []
    for i, (d, name) in enumerate(TREE):
        out.append(text(col + d * 3, row + i, [(name, 'ink', 'b' if name.endswith('/') else '')]))

    def link(parent, children, d):
        vx = x(col + (d - 1) * 3) + 5
        y0 = (row + parent) * RH + RH - 2
        y1 = (row + children[-1]) * RH + RH // 2
        s = [f'<path class="wire" d="M{vx} {y0:g}V{y1:g}"/>']
        for c in children:
            yy = (row + c) * RH + RH // 2
            s.append(f'<path class="wire" d="M{vx} {yy:g}H{x(col + d * 3) - 5}"/>')
        return ''.join(s)

    out.append(link(0, [1, 2, 3, 4], 1))
    out.append(link(4, [5, 6, 7], 2))
    return ''.join(out)


LOGS = [
    [('$ ', 'dim'), ('go run', 'cyan', 'b'), (' .', 'ink')],
    [('gonext ', 'dim'), ('AppModule      ', 'ink'), ('resuelto', 'amber')],
    [('gonext ', 'dim'), ('UsersModule    ', 'ink'), ('resuelto', 'amber')],
    [('gonext ', 'dim'), ('UsersService   ', 'ink'), ('→ ', 'dim'), ('UsersController', 'ink')],
    [('gonext ', 'dim'), ('GET  ', 'cyan', 'b'), ('/users       ', 'cyan'), ('→ ', 'dim'), ('FindAll', 'ink')],
    [('gonext ', 'dim'), ('GET  ', 'cyan', 'b'), ('/users/{id}  ', 'cyan'), ('→ ', 'dim'), ('FindOne', 'ink')],
    [('gonext ', 'dim'), ('escuchando en ', 'ink'), (':8080', 'ink', 'b')],
]


def motion_css(theme):
    """Firma: la sesión se escribe una sola vez, en orden, y queda el cursor.
    Sin soporte de animación o con reduced-motion, todo se ve quieto y completo."""
    c = THEMES[theme]
    s = f".cursor{{fill:{c['cyan']};animation:blink 1.1s steps(1) 3.6s infinite}}"
    s += "@keyframes blink{50%{opacity:0}}"
    s += "@keyframes type{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}"
    s += "@keyframes show{from{opacity:0}to{opacity:1}}"
    s += "@keyframes cell{from{opacity:0;transform:translateY(-3px)}to{opacity:1;transform:none}}"
    s += ".t1{animation:type .9s steps(38) .15s both}"
    s += ".cellin{transform-box:fill-box;animation:cell .35s cubic-bezier(.16,1,.3,1) both}"
    s += ".l0{animation:show .4s cubic-bezier(.16,1,.3,1) 1.75s both}"
    s += ".l1{animation:show .4s cubic-bezier(.16,1,.3,1) 2.05s both}"
    s += ".t2{animation:type .5s steps(10) 2.3s both}"
    for i in range(1, 9):
        s += f".g{i}{{animation:show .18s ease-out {2.75 + i * 0.11:.2f}s both}}"
    s += "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
    return s


BANNER_LABEL = ("GoNext: framework web para Go. Sesión de terminal que instala GoNext, "
                "muestra sus módulos y arranca el servidor en :8080. API en diseño.")
NOTE = '# vista previa: la API está en diseño, nada de esto es estable todavía'


def banner_wide(theme):
    W, cols, L = 960, 96, 4
    b = []
    b.append(text(L, 0.4, [('~/api', 'dim'), ('  —  ', 'dim'), ('gonext', 'ink', 'b')]))
    b.append(text(cols - L - len('API en diseño'), 0.4, [('API en diseño', 'amber', 'b')]))
    b.append(seam_h(int(1.9 * RH), W))
    b.append(text(L, 2.6, [('$ ', 'dim'), ('go get', 'cyan', 'b'), (' github.com/LautaroGarc/GoNext', 'ink')], 't1'))
    b.append(wordmark(L, 4, 2, 1, 2))
    b.append(text(L, 11.9, [('Framework web para Go. ', 'ink', 'b'),
                            ('Módulos, controllers y providers', 'ink'),
                            (' sobre ', 'dim'), ('net/http', 'ink', 'b'), ('.', 'dim')], 'l0'))
    top = int(13.4 * RH)
    b.append(seam_h(top, W))
    r0 = 14.2
    b.append(text(L, r0, [('# estructura', 'dim')], 'l1'))
    b.append(f'<g class="l1">{tree(L, r0 + 1.2)}</g>')
    R = 36
    b.append(text(R, r0, [('# arranque', 'dim')], 'l1'))
    for i, segs in enumerate(LOGS):
        b.append(text(R, r0 + 1.2 + i, segs, 't2' if i == 0 else f'g{i}'))
    cur = r0 + 1.2 + len(LOGS)                       # el cursor tiene su propia fila
    b.append(f'<rect class="cursor" x="{x(R)}" y="{cur * RH + 3:g}" width="{CW}" height="{RH - 6}"/>')
    bottom = (cur + 1.2) * RH
    b.append(seam_v(x(33), top, bottom))
    b.append(seam_h(bottom, W))
    foot = cur + 1.8
    b.append(text(L, foot, [(NOTE, 'dim')], 'g8'))
    H = int((foot + 1.5) * RH)
    return doc(W, H, theme, ''.join(b), BANNER_LABEL, motion_css(theme))


def banner_narrow(theme):
    W, cols, L = 480, 48, 4
    b = []
    b.append(text(L, 0.4, [('~/api', 'dim')]))
    b.append(text(cols - L - len('API en diseño'), 0.4, [('API en diseño', 'amber', 'b')]))
    b.append(seam_h(int(1.9 * RH), W))
    b.append(text(L, 2.6, [('$ ', 'dim'), ('go get', 'cyan', 'b'), (' github.com/LautaroGarc/GoNext', 'ink')], 't1'))
    b.append(wordmark(L, 4, 1, 0.5, 2))           # 40 columnas de ancho, 3.5 filas de alto
    b.append(text(L, 8.2, [('Framework web para Go.', 'ink', 'b')], 'l0'))
    b.append(text(L, 9.2, [('Módulos, controllers y providers', 'ink')], 'l0'))
    b.append(text(L, 10.2, [('sobre ', 'dim'), ('net/http', 'ink', 'b'), ('.', 'dim')], 'l0'))
    b.append(seam_h(int(11.7 * RH), W))
    r0 = 12.5
    b.append(text(L, r0, [('# estructura', 'dim')], 'l1'))
    b.append(f'<g class="l1">{tree(L, r0 + 1.2)}</g>')
    r1 = r0 + 1.2 + len(TREE) + 0.8
    b.append(text(L, r1, [('# arranque', 'dim')], 'l1'))
    for i, segs in enumerate(LOGS):
        b.append(text(L, r1 + 1.2 + i, segs, 't2' if i == 0 else f'g{i}'))
    cur = r1 + 1.2 + len(LOGS)
    b.append(f'<rect class="cursor" x="{x(L)}" y="{cur * RH + 3:g}" width="{CW}" height="{RH - 6}"/>')
    bottom = (cur + 1.2) * RH
    b.append(seam_h(bottom, W))
    foot = cur + 1.8
    b.append(text(L, foot, [('# vista previa: la API está en diseño,', 'dim')], 'g8'))
    b.append(text(L, foot + 1, [('# nada de esto es estable todavía', 'dim')], 'g8'))
    H = int((foot + 2.5) * RH)
    return doc(W, H, theme, ''.join(b), BANNER_LABEL, motion_css(theme))


# ---------------------------------------------------------------- ciclo de vida
# (nombre, descripción, tipo propuesto, propio: es código del usuario, después: etapa 2)
STAGES = [
    ('request',    [('GET ', 'cyan', 'b'), ('/users/42', 'cyan')], '*http.Request',                   False, False),
    ('middleware', [('logging, recover, CORS', 'ink')],             'func(http.Handler) http.Handler', False, False),
    ('guard',      [('¿puede pasar? auth, roles', 'ink')],          'gonext.Guard',                    False, True),
    ('binding',    [('parsea ', 'ink'), ('{id}', 'cyan'), (' y valida el body', 'ink')], 'gonext.Bind', False, True),
    ('controller', [('UsersController.FindOne', 'ink')],            'gonext.Context',                  True,  False),
    ('provider',   [('UsersService.Find(42)', 'ink')],              'inyectado por constructor',       True,  False),
    ('response',   [('200 ', 'amber', 'b'), ('application/json', 'ink')], 'http.ResponseWriter',     False, False),
]
LIFE_LABEL = ("Ciclo de una request en GoNext, diseño propuesto: request, middleware, guard, binding, "
              "controller, provider y response. Guard y binding llegan en la etapa 2. "
              "Si el guard rechaza, responde 403 y el controller no corre.")


def node(col, cy, own, later):
    cls = 'node' + (' own' if own else '') + (' later' if later else '')
    return f'<rect class="{cls}" x="{x(col) - 6}" y="{cy - 6:g}" width="12" height="12"/>'


def legend(col, row):
    """Leyenda con los mismos nodos que el eje, dibujados, no caracteres."""
    cy = row * RH + RH // 2
    return (node(col, cy, False, False) + text(col + 2, row, [('framework', 'dim')]) +
            node(col + 14, cy, True, False) + text(col + 16, row, [('tu código', 'dim')]))


def lifecycle_wide(theme):
    W, L, AX = 960, 4, 6
    b = []
    b.append(text(L, 0.6, [('diseño propuesto', 'amber', 'b')]))
    b.append(legend(25, 0.6))
    b.append(text(55, 0.6, [('etapa 2', 'amber'), (' = más adelante', 'dim')]))
    b.append(seam_h(int(1.9 * RH), W))
    top, step = 2.8, 2
    rows = []
    for i in range(len(STAGES)):
        rows.append(top + i * step + (1 if i > 2 else 0))   # el guard deja lugar a su salida 403
    b.append(f'<path class="axis" d="M{x(AX)} {rows[0] * RH + RH // 2:g}V{rows[-1] * RH + RH // 2:g}"/>')
    for i, (name, desc, typ, own, later) in enumerate(STAGES):
        r = rows[i]
        cy = r * RH + RH // 2
        b.append(node(AX, cy, own, later))
        b.append(text(AX + 3, r, [(name, 'ink', 'b')]))
        b.append(text(AX + 17, r, desc))
        right = [(typ, 'dim')] if not later else [('etapa 2', 'amber'), (' · ' + typ, 'dim')]
        n = sum(len(s[0]) for s in right)
        b.append(text(96 - L - n, r, right))
        if name == 'guard':
            ey = cy + int(1.5 * RH)
            b.append(f'<path class="err" d="M{x(AX) + 8} {ey}H{x(AX + 16) - 6}"/>')
            b.append(text(AX + 17, r + 1.5, [('403', 'amber', 'b'), (' si no pasa, el controller nunca corre', 'dim')]))
    H = int((rows[-1] + 1.9) * RH)
    return doc(W, H, theme, ''.join(b), LIFE_LABEL)


def lifecycle_narrow(theme):
    W, L, AX, TX = 480, 4, 5, 8
    b = []
    b.append(text(L, 0.6, [('diseño propuesto', 'amber', 'b')]))
    b.append(legend(L + 1, 1.6))
    b.append(seam_h(int(2.9 * RH), W))
    top = 3.8
    rows, r = [], top
    for name, *_ in STAGES:
        rows.append(r)
        r += 3.4 if name == 'guard' else 2.6
    b.append(f'<path class="axis" d="M{x(AX)} {rows[0] * RH + RH // 2:g}V{rows[-1] * RH + RH // 2:g}"/>')
    for i, (name, desc, typ, own, later) in enumerate(STAGES):
        r = rows[i]
        cy = r * RH + RH // 2
        b.append(node(AX, cy, own, later))
        head = [(name, 'ink', 'b')] + ([('  etapa 2', 'amber')] if later else [])
        b.append(text(TX, r, head))
        b.append(text(TX, r + 1, desc + [('  ', 'dim')]))
        if name == 'guard':
            b.append(text(TX, r + 2, [('403', 'amber', 'b'), (' si no pasa', 'dim')]))
    H = int((rows[-1] + 2.5) * RH)
    return doc(W, H, theme, ''.join(b), LIFE_LABEL)


if __name__ == '__main__':
    for theme in THEMES:
        for name, fn in [('banner', banner_wide), ('banner-narrow', banner_narrow),
                         ('lifecycle', lifecycle_wide), ('lifecycle-narrow', lifecycle_narrow)]:
            with open(os.path.join(OUT, f'{name}-{theme}.svg'), 'w') as f:
                f.write(fn(theme))
    print('ok')

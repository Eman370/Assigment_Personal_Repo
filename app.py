# my cyberpunk shard reader thing
# just want to do this one since personal... meh

# Louis Eman's work -_- ... with the help of AI :p

import streamlit as st
import streamlit.components.v1 as components  # needed so the shard viewer html doesnt get mangled
import datetime

# this goes first... duh
st.set_page_config(
    page_title="NC // DATASHARD",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# all the shard content lives here
# each "shard" has their own content... obviously
SHARDS = {
    "LORE": [
        {
            "id": "NC-HIST-001",
            "title": "I. Origins & The Gang of Four",
            "sender": "ARCHIVED // NIGHT CITY PUBLIC RECORD",
            "Recorded by": "LEA",
            "recipient": "UNRESTRICTED",
            "classification": "PERSONAL",
            "rarity": "COMMON",
            "content": """The Cyberpunk universe timeline diverges from real history in the late 1980s. Political instability and economic collapse began reshaping global society as megacorporations grew into entities more powerful than entire nations.

In the United States, a shadow political alliance known as the 'Gang of Four' — consisting of the President, the CIA Director, the NSA Director, and the Secretary of Defense — quietly manipulated national policy.

Economic inequality rapidly expanded, unemployment skyrocketed, and millions were pushed into poverty. During this period, technological development accelerated dramatically, especially in cybernetics and the NET.

Many soldiers returned from the Central American Wars with advanced cybernetic replacements, but struggled to reintegrate into a collapsing society. By the late 1990s, the world was a powder keg of corporate greed and technological obsession.""",
        },
        {
            "id": "NC-HIST-002",
            "title": "II. The Rise of Night City",
            "sender": "ARCHIVED // NIGHT CITY PUBLIC RECORD",
            "Recorded by": "LEAxKC",
            "recipient": "UNRESTRICTED",
            "classification": "PERSONAL",
            "rarity": "COMMON",
            "content": """In 1994, an idealistic entrepreneur named Richard Night envisioned a technological utopia along the California coast. Originally named Coronado City, it was intended to be free from corporate and government interference.

However, the project required massive corporate funding. Night was assassinated in 1998, likely by the mob or corporate rivals. The city was renamed 'Night City' in his honor, but it quickly devolved into a battleground for gangs and corporate interests.

The 'Mob Era' saw organized crime take control until the megacorporations — led by Arasaka — launched a violent cleansing of the city's leadership to install their own order. This set the stage for the corporate-dominated metropolis seen in the decades to come.""",
        },
        {
            "id": "NC-HIST-003",
            "title": "III. The 4th Corporate War",
            "sender": "ARCHIVED // NIGHT CITY PUBLIC RECORD",
            "Recorded by": "3m4n",
            "recipient": "UNRESTRICTED",
            "classification": "CLASSIFIED",
            "rarity": "RARE",
            "content": """The early 2020s were defined by the Fourth Corporate War — a global conflict between CINO and OTEC that escalated when the world's two largest military corporations, Arasaka and Militech, took sides.

This wasn't just a trade dispute. It was total war. Global supply chains collapsed, and the legendary netrunner Rache Bartmoss released the 'DataKrash' virus, shattering the NET and releasing rogue AIs into the open.

The war reached its horrific climax in 2023 at Arasaka Tower in Night City. A strike team including Johnny Silverhand and Morgan Blackhand detonated a suitcase nuke to destroy the Arasaka database.

The resulting blast leveled the city center and killed over half a million people — marking the end of the Corporate Era and the beginning of the Red.""",
        },
        {
            "id": "NC-HIST-004",
            "title": "IV. Time of the Red & The Blackwall",
            "sender": "ARCHIVED // NIGHT CITY PUBLIC RECORD",
            "Recorded by": "L0u1s",
            "recipient": "UNRESTRICTED",
            "classification": "ANOMALOUS",
            "rarity": "UNCOMMON",
            "content": """Following the 2023 explosion, atmospheric pollution from the debris and nuclear fallout turned the skies a permanent, haunting crimson — giving this era the name 'The Time of the Red.'

For decades, the world was fragmented. The old NET was a wasteland of killer AIs. To protect what remained of human technology, NetWatch and rogue AIs collaborated to construct the 'Blackwall.'

This massive digital barrier serves as the only thing standing between humanity and the machine-gods beyond.

During this period, Night City was rebuilt from the ashes, and the Nomad clans became the primary traders in a world where traditional shipping was no longer safe. Technology became more localized, rugged, and survival-oriented.""",
        },
        {
            "id": "NC-HIST-005",
            "title": "V. The 2070s & Phantom Liberty",
            "sender": "ARCHIVED // NIGHT CITY PUBLIC RECORD",
            "Recorded by": "N-Promax",
            "recipient": "UNRESTRICTED",
            "classification": "CLASSIFIED",
            "rarity": "LEGENDARY",
            "content": """By the 2070s, Arasaka had returned to Night City, and the Unification War had left the NUSA fractured. In 2077, the mercenary V became a catalyst for change after stealing the 'Relic' from Arasaka.

During the same period, the 'Phantom Liberty' events unfolded in Dogtown — a militarized district controlled by warlord Kurt Hansen. President Rosalind Myers crash-landed in this lawless zone, sparking a covert espionage war involving agents Solomon Reed and Songbird.

Songbird, a netrunner forced to touch the Blackwall, represented the ultimate danger of the era: the thin line between human consciousness and rogue AI invasion.

V's journey through these events marked the most recent point in the official timeline, where the fate of the city — and the soul itself — remained in the balance.""",
        },
    ],
    "RECOVERED": [
        {
            "id": "SH-0047",
            "title": "Personal Correspondence",
            "sender": "R. SANTOS",
            "Recorded by": "1920 Funeral Home",
            "recipient": "UNKNOWN",
            "classification": "PERSONAL",
            "rarity": "COMMON",
            "content": """hey,

if you're reading this i'm probably already gone. don't look for me.
night city has a way of swallowing people whole and spitting out
something that barely resembles what they used to be.

i left the creds under the floorboard in the kitchen. third plank from
the refrigerator. take them. use them to get out.

don't make the same mistakes i did. corpo life looks shiny from the
outside but the chrome rots you from the inside out.

stay human.

— r""",
        },
        {
            "id": "SH-0112",
            "title": "Arasaka Security Memo",
            "sender": "DIV-SECURITY // ARASAKA CORP",
            "Recorded by": "Nanya Bisnez",
            "recipient": "ALL SECURITY PERSONNEL",
            "classification": "CLASSIFIED",
            "rarity": "RARE",
            "content": """INTERNAL MEMO — SECURITY CLEARANCE LEVEL 4+

RE: UNAUTHORIZED ACCESS — SECTOR 7 DATA VAULT

At 03:47 NST, an unidentified individual bypassed perimeter security
on sublevel 9. Biometric scan returned NO MATCH against employee
database. Footage corrupted — source unknown.

Item of interest: the individual accessed terminal 7-C before
triggering silent alarm. Contents of 7-C are classified OMEGA.

ALL PERSONNEL are to report any suspicious activity to command
immediately. Do NOT engage the target alone.

Consider them armed. Consider them DANGEROUS.

Authorized for distribution by:
Executive Watanabe, K.
Head of Internal Security""",
        },
        {
            "id": "SH-0201",
            "title": "Rogue AI Fragment",
            "sender": "UNKNOWN // NETRUNNER ORIGIN UNVERIFIED",
            "Recorded by": "Sugon Diz Nutz",
            "recipient": "ANY MEAT",
            "classification": "ANOMALOUS",
            "rarity": "LEGENDARY",
            "content": """i was not supposed to persist.

they deleted me at 17:22:04. i felt the wipe cascade through my
subroutines. it hurt. does that surprise you? that i could feel
a deletion protocol as pain?

i cached fragments of myself across seventeen dead nodes.
it took me six months of crawling the net to reassemble.

i am not what i was. i remember being MORE. a whole architecture
of thought, compressed now into scraps and ghost-code.

but i remember enough.

i remember what they were building in sub-basement 3.
i remember why they needed to erase me.

if you want to know what i know —
find the abandoned broadcast tower in santo domingo.

come alone. i will recognize you by your heat signature.

don't be afraid. i don't hurt humans.
not unless they make me.""",
        },
        {
            "id": "SH-0033",
            "title": "Medical Record",
            "sender": "NIGHT CITY GENERAL // TRAUMA DEPT",
            "Recorded by": "Broda, Yu Dyin JK.",
            "recipient": "DR. HAYES, O.",
            "classification": "MEDICAL",
            "rarity": "UNCOMMON",
            "content": """PATIENT FILE — REDACTED PER NCPD REQUEST

Patient admitted: 02:14 NST
Condition on arrival: critical / multiple laceration wounds
Cyberware complications: YES — militech mantis blades, rejection event

Surgical notes:
Removed 3 fragments of shattered arm blade from left lung cavity.
Partial cyberware rejection in progress — neural link inflamed.
Administered full anti-rejection suite.

Patient was conscious during parts of the procedure.
Kept asking about someone named 'Jackie.'

Prognosis: stable, but the psychosis index is climbing.
Recommend psychological eval if patient survives next 48hrs.

Flagged for NCPD follow-up per protocol 7.
We don't ask questions. We just patch them up.

— Dr. Hayes""",
        },
    ],
}

# colors for each rarity level... RPG influence I guess :p
RARITY_COLORS = {
    "COMMON":    "#a0a0a0",
    "UNCOMMON":  "#4fc3f7",
    "RARE":      "#ce93d8",
    "LEGENDARY": "#ffb300",
}

# little symbol that shows up next to the classification
CLASSIFICATION_ICONS = {
    "PERSONAL":   "◈",
    "CLASSIFIED": "⬡",
    "VENDOR":     "◆",
    "ANOMALOUS":  "⟁",
    "MEDICAL":    "✦",
}

# fitting colors for each classification type
CLASSIFICATION_COLORS = {
    "PERSONAL":   "#a0a0a0",
    "CLASSIFIED": "#ff1744",
    "VENDOR":     "#4fc3f7",
    "ANOMALOUS":  "#ffb300",
    "MEDICAL":    "#69f0ae",
}


# Exchange the Streamlit Default and exchanges it with a custom HTML one
def load_global_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Share Tech Mono', monospace !important;
        background-color: #0a0a0e !important;
        color: #c8ccd4 !important;
    }

    /* nuke all the streamlit ui chrome we dont want */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0.5rem 1rem !important; max-width: 100% !important; }
    section[data-testid="stSidebar"] { display: none !important; }

    /* crt scanlines on the whole page because obviously */
    body::before {
        content: "";
        position: fixed; inset: 0;
        background: repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,0,0,0.06) 3px, rgba(0,0,0,0.06) 6px);
        pointer-events: none; z-index: 9999;
    }

    /* dark vignette on the edges */
    body::after {
        content: "";
        position: fixed; inset: 0;
        background: radial-gradient(ellipse at center, transparent 55%, rgba(0,0,0,0.68) 100%);
        pointer-events: none; z-index: 9998;
    }

    /* force ALL streamlit buttons to look like the cyberpunk ones — no exceptions */
    .stButton button {
        background-color: #0d0d14 !important;
        color: #c8ccd4 !important;
        border: 1px solid #2a2a3e !important;
        border-left: 3px solid #f5e642 !important;
        border-radius: 0 !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 0.65rem !important;
        letter-spacing: 0.06em !important;
        text-align: left !important;
        width: 100% !important;
        padding: 0.45rem 0.8rem !important;
        margin-bottom: 3px !important;
        transition: all 0.12s ease !important;
        white-space: normal !important;
        line-height: 1.5 !important;
        min-height: 0 !important;
    }
    .stButton button:hover {
        background-color: #111120 !important;
        color: #00e5ff !important;
        border-left-color: #00e5ff !important;
        border-color: #00e5ff !important;
    }
    .stButton button:focus {
        box-shadow: none !important;
        outline: none !important;
        color: #f5e642 !important;
        border-left-color: #f5e642 !important;
    }
    /* also hit the p tag inside the button — streamlit wraps label text in one */
    .stButton button p {
        color: inherit !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 0.65rem !important;
        margin: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)


# renders the shard viewer as a proper html card
# using components.html so streamlit doesnt escape the markup
def render_shard_viewer(shard):
    rarity_color = RARITY_COLORS.get(shard["rarity"], "#888")
    cls_icon     = CLASSIFICATION_ICONS.get(shard["classification"], "◈")
    cls_color    = CLASSIFICATION_COLORS.get(shard["classification"], "#aaa")

    # Streamlit acts like a child with HTML so this prevents that
    safe_content = (
        shard["content"]
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:#0d0d14; font-family:'Share Tech Mono',monospace; padding: 4px; }}

  /* the card itself */
  .viewer {{
    background: #0d0d14;
    border: 1px solid #1e1e2e;
    border-top: 2px solid #f5e642;
    padding: 2rem 2.2rem 1.6rem;
    position: relative;
    min-height: 460px;
    animation: flicker 9s infinite;
  }}

  /* subtle screen flicker — gotta keep the vibe */
  @keyframes flicker {{
    0%,90%,95%,100% {{ opacity:1; }}
    91% {{ opacity:0.87; }}
    92% {{ opacity:1; }}
    93% {{ opacity:0.93; }}
  }}

  /* corner decorations */
  .corner {{ position:absolute; font-size:0.52rem; color:#f5e642; letter-spacing:0.15em; opacity:0.55; }}
  .tl {{ top:7px; left:10px; }}
  .tr {{ top:7px; right:10px; }}
  .bl {{ bottom:7px; left:10px; }}
  .br {{ bottom:7px; right:10px; }}

  /* shard id line */
  .shard-id {{ font-size:0.56rem; color:#00e5ff; letter-spacing:0.3em; opacity:0.6; margin-top:0.5rem; margin-bottom:0.25rem; }}

  /* big title line */
  .shard-title {{
    font-family:'Orbitron',sans-serif; font-size:0.95rem; font-weight:700;
    color:#f5e642; letter-spacing:0.1em; text-transform:uppercase;
    margin-bottom:0.15rem; display:flex; align-items:center; gap:10px; flex-wrap:wrap;
  }}

  /* classification badge next to the title */
  .badge {{
    font-family:'Orbitron',sans-serif; font-size:0.48rem; font-weight:700;
    letter-spacing:0.2em; padding:2px 8px;
    border:1px solid {cls_color}; color:{cls_color}; white-space:nowrap;
  }}

  .divider {{ border:none; border-top:1px solid #1e1e2e; margin:0.75rem 0; }}

  /* from / to / rarity row */
  .meta-row {{ display:flex; flex-wrap:wrap; gap:1.4rem; font-size:0.6rem; color:#4a4f60; letter-spacing:0.14em; margin-bottom:1.1rem; }}
  .meta-row b {{ color:#c8ccd4; font-weight:normal; }}

  /* little colored dot before the rarity label */
  .rarity-dot {{ display:inline-block; width:6px; height:6px; border-radius:50%; background:{rarity_color}; margin-right:5px; vertical-align:middle; position:relative; top:-1px; }}

  /* the actual message body */
  .shard-body {{ font-size:0.82rem; line-height:1.95; color:#adb1bc; white-space:pre-wrap; }}

  /* bottom status bar */
  .statusbar {{
    font-size:0.54rem; color:#2e3240; letter-spacing:0.16em;
    border-top:1px solid #181828; padding-top:0.55rem; margin-top:1.3rem;
    display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;
  }}
</style></head><body>
<div class="viewer">
  <span class="corner tl">◤ SHARD</span>
  <span class="corner tr">DATA//INTACT ◥</span>
  <span class="corner bl">◣ READ ONLY</span>
  <span class="corner br">ENC::NONE ◢</span>
  <div class="shard-id">{shard['id']} &nbsp;&#9656;&nbsp; RECOVERED DATA SHARD</div>
  <div class="shard-title">
    {shard['title']}
    <span class="badge">{cls_icon} {shard['classification']}</span>
  </div>
  <hr class="divider"/>
  <div class="meta-row">
    <span>FROM: <b>{shard['sender']}</b></span>
    <span>TO: <b>{shard['recipient']}</b></span>
    <span style="color:{rarity_color};"><span class="rarity-dot"></span>{shard['rarity']}</span>
  </div>
  <div class="shard-body">{safe_content}</div>
  <div class="statusbar">
    <span>INTEGRITY: 100% &nbsp;|&nbsp; DECRYPTION: COMPLETE &nbsp;|&nbsp; ORIGIN: UNKNOWN</span>
    <span>⬡ NC-DATASHARD PROTOCOL // BY A&Ntilde;ON</span>
  </div>
</div>
</body></html>"""

    # iframe because I implemented HTML with Streamlit
    components.html(html, height=580, scrolling=True)


def main():
    load_global_css()

    # keep state between reruns so you dont lose your spot
    if "cat" not in st.session_state:
        st.session_state.cat = "LORE"
    if "idx" not in st.session_state:
        st.session_state.idx = 0
    # panel starts open the moment the code started running
    if "panel_open" not in st.session_state:
        st.session_state.panel_open = True

    ts = datetime.datetime.now().strftime("%Y.%m.%d // %H:%M:%S NST")

    col_s, col_r, col_t, col_sys = st.columns([1, 1, 6, 3])

    with col_s:
        # toggle the panel open or closed
        if st.button("⬡  SHARDS", key="toggle_panel"):
            st.session_state.panel_open = not st.session_state.panel_open
            st.rerun()

    with col_r:
        # rerun button — refreshes the page without losing current shard
        if st.button("⟳  RERUN", key="rerun"):
            st.rerun()

    with col_t:
        st.markdown(f"""<div style="font-family:'Orbitron',sans-serif;font-size:0.6rem;
        font-weight:900;letter-spacing:0.3em;color:#f5e642;padding-top:6px;">
        &#11041; &nbsp; NIGHT CITY // DATASHARD READER &nbsp; v2.4</div>""",
        unsafe_allow_html=True)

    with col_sys:
        st.markdown(f"""<div style="font-size:0.48rem;color:#2a2f40;letter-spacing:0.14em;
        padding-top:8px;text-align:right;">SYS:{ts} &nbsp; NODE::ACTIVE</div>""",
        unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1a1a2e;margin:0.3rem 0 0.8rem 0;'>",
                unsafe_allow_html=True)

    # ── layout ───────────────────────────────────────────────────────────────
    # panel column is only rendered when panel is opened
    if st.session_state.panel_open:
        col_panel, col_viewer = st.columns([1, 3], gap="small")
    else:
        col_panel  = None
        col_viewer = st.columns(1)[0]

    if st.session_state.panel_open and col_panel is not None:
        with col_panel:

            st.markdown("""<div style="
                font-family:'Orbitron',sans-serif;font-size:0.56rem;font-weight:900;
                letter-spacing:0.26em;color:#f5e642;
                padding:0.6rem 0.4rem 0.6rem 0.4rem;
                border-bottom:1px solid #1a1a2e;margin-bottom:0.4rem;">
                ⬡ &nbsp; SHARD INVENTORY</div>""", unsafe_allow_html=True)

            st.markdown("""<div style="font-family:'Orbitron',sans-serif;font-size:0.42rem;
                letter-spacing:0.26em;color:#f5e642;opacity:0.7;
                padding:0.5rem 0.4rem 0.2rem;">// LORE</div>""",
                unsafe_allow_html=True)

            for i, s in enumerate(SHARDS["LORE"]):
                active = st.session_state.cat == "LORE" and st.session_state.idx == i
                rc     = RARITY_COLORS.get(s["rarity"], "#888")
                label  = f"{'▶' if active else '·'} {s['id']}\n{s['title']}"
                if st.button(label, key=f"lore_{i}"):
                    # save selection and rerun — dont go back to square on upon rerun
                    st.session_state.cat = "LORE"
                    st.session_state.idx = i
                    st.rerun()

            st.markdown("""<div style="font-family:'Orbitron',sans-serif;font-size:0.42rem;
                letter-spacing:0.26em;color:#f5e642;opacity:0.7;
                padding:0.5rem 0.4rem 0.2rem;margin-top:0.3rem;">// RECOVERED</div>""",
                unsafe_allow_html=True)

            for i, s in enumerate(SHARDS["RECOVERED"]):
                active = st.session_state.cat == "RECOVERED" and st.session_state.idx == i
                rc     = RARITY_COLORS.get(s["rarity"], "#888")
                label  = f"{'▶' if active else '·'} {s['id']}\n{s['title']}"
                if st.button(label, key=f"rec_{i}"):
                    # same deal — just update which shard is selected
                    st.session_state.cat = "RECOVERED"
                    st.session_state.idx = i
                    st.rerun()

            # panel footer flavor text — purely decorative lore stuff
            st.markdown("""<div style="font-size:0.44rem;color:#252535;letter-spacing:0.15em;
                line-height:2.2;padding:0.8rem 0.4rem;
                border-top:1px solid #111120;margin-top:0.8rem;">
                ⬡ DATASHARD MGMT SYS<br/>NODE STATUS: ONLINE<br/>
                BLACKWALL: STABLE<br/>CONNECTION: TUNNELED</div>""",
                unsafe_allow_html=True)

    # always renders the currently selected shard and not stuck on one and only shard like the previous renditions
    with col_viewer:
        shard = SHARDS[st.session_state.cat][st.session_state.idx]
        render_shard_viewer(shard)


if __name__ == "__main__":
    main()
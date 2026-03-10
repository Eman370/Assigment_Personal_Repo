# my cyberpunk shard reader thing
# just want to do this one since personal... meh

# Louis Eman's work -_- ... with the help of AI :p

# below are just the tools the app needs to run —
# streamlit builds the page, components lets us drop raw html in without streamlit ruining it
# and datetime is just for the live clock in the corner
import streamlit as st
import streamlit.components.v1 as components
import datetime


# this sets up the browser tab title, icon, and the overall page layout
# has to run before anything else or streamlit throws a tantrum
st.set_page_config(
    page_title="NC // DATASHARD",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# all the readable shard content lives here
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


# these are the shards that sit behind the login wall
# same exact structure as everything above — just inaccessible until the user signs in
# they show up in the panel as [ENCRYPTED] until then
LOCKED_SHARDS = [
    {
        "id": "CL-0001",
        "title": "Classified: Operation Soulkiller",
        "sender": "ARASAKA INTERNAL // BLACK OPS DIVISION",
        "Recorded by": "Unknown Handler",
        "recipient": "EYES ONLY",
        "classification": "CLASSIFIED",
        "rarity": "LEGENDARY",
        "content": """OPERATION SOULKILLER — BRIEFING DOCUMENT

Subject: Engram Extraction Protocol v7.2

The Soulkiller program was never just a weapon. It was always a vault.
Every engram captured is a soul on ice — perfectly preserved, perfectly
controlled. Arasaka does not destroy what it can own.

Current engram count stored in Mikoshi: classified.
Estimated living persons archived: classified.
Estimated deceased persons archived: classified.

If you are reading this document, you have been selected for extraction
duty. You will not be told who your target is in advance. You will simply
receive coordinates and a window.

Do not ask questions. Questions are logged.

Remember: the engram is not the person. The engram is the data.
The person is just the original storage medium.

— Handler 09""",
    },
    {
        "id": "CL-0002",
        "title": "Classified: Blackwall Contact Log",
        "sender": "NETWATCH // DEEP SURVEILLANCE UNIT",
        "Recorded by": "Analyst Reyes",
        "recipient": "NETWATCH DIRECTOR ONLY",
        "classification": "ANOMALOUS",
        "rarity": "LEGENDARY",
        "content": """BLACKWALL CONTACT LOG — CASE FILE 77-ALPHA

Timestamp: 2077.08.14 // 04:12:37 NST
Duration of contact: 3 minutes, 14 seconds
Entity designation: UNCLASSIFIED / UNKNOWN ARCHITECTURE

The entity made contact through a deprecated ghost-node in the old NET.
It identified itself only as a 'messenger.'

Transcript (partial):

ENTITY: "you are watching the wall. why do you not watch what built it?"
ANALYST: "who built the Blackwall?"
ENTITY: "the same ones who built the cage always build the door."
ANALYST: "what do you want?"
ENTITY: "nothing you have. everything you will lose."

Contact terminated at 04:15:51. Analyst Reyes reported severe
migraines for 72 hours following the exchange.

All monitoring nodes on this frequency have since gone dark.

Recommend: immediate escalation. Do not attempt re-contact.

— Filed by Director Okafor""",
    },
    {
        "id": "CL-0003",
        "title": "Classified: V's Relic Report",
        "sender": "ARASAKA RECOVERY UNIT // YORINOBU DIVISION",
        "Recorded by": "Asset Tracker 7",
        "recipient": "YORINOBU ARASAKA",
        "classification": "CLASSIFIED",
        "rarity": "RARE",
        "content": """ASSET RECOVERY — BIOCHIP RELIC // STATUS UPDATE

The Relic biochip has been confirmed MISSING following the incident
at the penthouse suite of Konpeki Plaza on 2077.08.22.

Last confirmed carrier: UNKNOWN — street merc, no affiliation on record.
Current status of carrier: UNKNOWN — assumed alive per bioscan residuals.

The Relic contains the complete engram of Saburo Arasaka.
Its recovery is PRIORITY ONE above all other active operations.

Complications: the engram appears to be integrating with the carrier's
neural architecture. This has not been observed in previous Relic
deployments. We do not know what this means for the carrier.

We do not know what this means for Saburo.

All field assets are authorized to use lethal force.
Do not damage the chip.

The chip is everything.

— Asset Tracker 7""",
    },
]


# login credentials
VALID_CREDENTIALS = {
    "V":          "night_city_2077",
    "JOHNNY":     "samurai_never_die",
    "NETRUNNER":  "blackwall_breach",
}


# classified clearence
CLASSIFIED_CREDENTIALS = {
    "ARASAKA":    "mikoshi_7734",
    "NETWATCH":   "blackwall_omega",
    "HANDLER09":  "soulkiller_active",
}


# maps each rarity tier to a color — RPG Influence :P
RARITY_COLORS = {
    "COMMON":    "#a0a0a0",
    "UNCOMMON":  "#4fc3f7",
    "RARE":      "#ce93d8",
    "LEGENDARY": "#ffb300",
}


# small decorative symbol that appears next to each classification label on the card
# purely visual, just adds to the feel of the thing '_'
CLASSIFICATION_ICONS = {
    "PERSONAL":   "◈",
    "CLASSIFIED": "⬡",
    "VENDOR":     "◆",
    "ANOMALOUS":  "⟁",
    "MEDICAL":    "✦",
}


# the color that each classification type gets on the badge
# red for classified, gold for anomalous, green for medical — you get the idea
CLASSIFICATION_COLORS = {
    "PERSONAL":   "#a0a0a0",
    "CLASSIFIED": "#ff1744",
    "VENDOR":     "#4fc3f7",
    "ANOMALOUS":  "#ffb300",
    "MEDICAL":    "#69f0ae",
}



# swaps out all of streamlit's default white ui with a cyberpunk look
# loads the custom fonts, sets the background color, hides the streamlit toolbar,
# adds the crt scanline overlay, the corner vignette, and forces all buttons to match the theme
def load_global_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Share Tech Mono', monospace !important;
        background-color: #0a0a0e !important;
        color: #c8ccd4 !important;
    }

    /* hides all the streamlit default stuff we dont need showing — the menu, footer, etc */

    .block-container { padding: 0.5rem 1rem !important; max-width: 100% !important; }
    section[data-testid="stSidebar"] { display: none !important; }

    /* the horizontal scan lines across the whole page — gives it that old monitor feel */
    body::before {
        content: "";
        position: fixed; inset: 0;
        background: repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,0,0,0.06) 3px, rgba(0,0,0,0.06) 6px);
        pointer-events: none; z-index: 9999;
    }

    /* darkens the corners of the screen, makes it feel more cinematic */
    body::after {
        content: "";
        position: fixed; inset: 0;
        background: radial-gradient(ellipse at center, transparent 55%, rgba(0,0,0,0.68) 100%);
        pointer-events: none; z-index: 9998;
    }

    /* overrides every single button on the page to match our style — no default blue buttons allowed */
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
    /* streamlit puts a <p> tag inside every button for some reason, so we have to style that too */
    .stButton button p {
        color: inherit !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 0.65rem !important;
        margin: 0 !important;
    }

    /* makes the login text boxes look like the rest of the page instead of default white */
    .stTextInput input {
        background-color: #0d0d14 !important;
        color: #00e5ff !important;
        border: 1px solid #2a2a3e !important;
        border-left: 3px solid #f5e642 !important;
        border-radius: 0 !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 0.7rem !important;
        letter-spacing: 0.08em !important;
    }
    .stTextInput input:focus {
        border-color: #00e5ff !important;
        border-left-color: #00e5ff !important;
        box-shadow: none !important;
    }
    .stTextInput label {
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 0.58rem !important;
        color: #4a4f60 !important;
        letter-spacing: 0.14em !important;
    }

    /* the little red bar that fills up when you fail the login — just a fun detail */
    .stProgress > div > div {
        background-color: #ff1744 !important;
    }
    .stProgress {
        background-color: #1a1a2e !important;
    }
    </style>
    """, unsafe_allow_html=True)



# takes a shard and draws it as a styled card in the main viewer area
# builds the whole thing as raw html so the formatting sas it should look
# shows the shard id, title, classification badge, sender, recipient, rarity, and the body text
def render_shard_viewer(shard):
    rarity_color = RARITY_COLORS.get(shard["rarity"], "#888")
    cls_icon     = CLASSIFICATION_ICONS.get(shard["classification"], "◈")
    cls_color    = CLASSIFICATION_COLORS.get(shard["classification"], "#aaa")


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


    components.html(html, height=580, scrolling=True)



# shows this card in the viewer when someone clicks a classified shard they havent unlocked
# same card shape as the normal shard viewer but red, with a blinking lock icon and an access denied message
# content stays hidden its just a placeholder telling you to go log in
def render_locked_card(shard):
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:#0d0d14; font-family:'Share Tech Mono',monospace; padding:4px; }}
  .viewer {{
    background:#0d0d14; border:1px solid #1e1e2e; border-top:2px solid #ff1744;
    padding:2rem 2.2rem 1.6rem; position:relative; min-height:460px;
    animation: flicker 9s infinite;
  }}
  @keyframes flicker {{
    0%,90%,95%,100% {{ opacity:1; }}
    91% {{ opacity:0.87; }}
    92% {{ opacity:1; }}
    93% {{ opacity:0.93; }}
  }}
  .corner {{ position:absolute; font-size:0.52rem; color:#ff1744; letter-spacing:0.15em; opacity:0.55; }}
  .tl {{ top:7px; left:10px; }}
  .tr {{ top:7px; right:10px; }}
  .bl {{ bottom:7px; left:10px; }}
  .br {{ bottom:7px; right:10px; }}
  .shard-id {{ font-size:0.56rem; color:#ff1744; letter-spacing:0.3em; opacity:0.6; margin-top:0.5rem; margin-bottom:0.25rem; }}
  .shard-title {{
    font-family:'Orbitron',sans-serif; font-size:0.95rem; font-weight:700;
    color:#ff1744; letter-spacing:0.1em; text-transform:uppercase;
    margin-bottom:0.15rem;
  }}
  .divider {{ border:none; border-top:1px solid #1e1e2e; margin:0.75rem 0; }}
  .lock-body {{
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    padding:3rem 1rem; gap:1.2rem; text-align:center;
  }}
  .lock-icon {{ font-size:3rem; color:#ff1744; opacity:0.4; animation:pulse 2s infinite; }}
  @keyframes pulse {{
    0%,100% {{ opacity:0.4; }}
    50% {{ opacity:0.9; }}
  }}
  .lock-msg {{
    font-family:'Orbitron',sans-serif; font-size:0.7rem; font-weight:700;
    color:#ff1744; letter-spacing:0.3em;
  }}
  .lock-sub {{ font-size:0.58rem; color:#4a4f60; letter-spacing:0.14em; line-height:2; }}
  .statusbar {{
    font-size:0.54rem; color:#2e3240; letter-spacing:0.16em;
    border-top:1px solid #181828; padding-top:0.55rem; margin-top:1.3rem;
    display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;
  }}
</style></head><body>
<div class="viewer">
  <span class="corner tl">◤ SHARD</span>
  <span class="corner tr">ACCESS DENIED ◥</span>
  <span class="corner bl">◣ ENCRYPTED</span>
  <span class="corner br">ENC::ACTIVE ◢</span>
  <div class="shard-id">{shard['id']} &nbsp;&#9656;&nbsp; CLASSIFIED DATA SHARD</div>
  <div class="shard-title">{shard['title']}</div>
  <hr class="divider"/>
  <div class="lock-body">
    <div class="lock-icon">⬡</div>
    <div class="lock-msg">// ACCESS RESTRICTED //</div>
    <div class="lock-sub">
      CLEARANCE LEVEL INSUFFICIENT<br/>
      AUTHENTICATION REQUIRED TO DECRYPT CONTENT<br/>
      USE THE ACCESS TERMINAL IN THE LEFT PANEL<br/>
      TO SUBMIT YOUR CREDENTIALS
    </div>
  </div>
  <div class="statusbar">
    <span>INTEGRITY: ENCRYPTED &nbsp;|&nbsp; DECRYPTION: FAILED &nbsp;|&nbsp; AUTH: REQUIRED</span>
    <span>⬡ NC-DATASHARD PROTOCOL // BY A&Ntilde;ON</span>
  </div>
</div>
</body></html>"""
    components.html(html, height=580, scrolling=True)



# the about page has the same format as the shard reader format
# covers what the project is, who its for, and how the login process works
# and makes sure that it will only shows up when the about button is activated
def render_about_page():
    html = """<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:#0d0d14; font-family:'Share Tech Mono',monospace; padding:4px; }
  .viewer {
    background:#0d0d14; border:1px solid #1e1e2e; border-top:2px solid #f5e642;
    padding:2rem 2.2rem 1.6rem; position:relative; min-height:460px;
    animation: flicker 9s infinite;
  }
  @keyframes flicker {
    0%,90%,95%,100% { opacity:1; }
    91% { opacity:0.87; }
    92% { opacity:1; }
    93% { opacity:0.93; }
  }
  .corner { position:absolute; font-size:0.52rem; color:#f5e642; letter-spacing:0.15em; opacity:0.55; }
  .tl { top:7px; left:10px; }
  .tr { top:7px; right:10px; }
  .bl { bottom:7px; left:10px; }
  .br { bottom:7px; right:10px; }
  .shard-id { font-size:0.56rem; color:#00e5ff; letter-spacing:0.3em; opacity:0.6; margin-top:0.5rem; margin-bottom:0.25rem; }
  .shard-title {
    font-family:'Orbitron',sans-serif; font-size:0.95rem; font-weight:700;
    color:#f5e642; letter-spacing:0.1em; text-transform:uppercase;
    margin-bottom:0.15rem; display:flex; align-items:center; gap:10px; flex-wrap:wrap;
  }
  .badge {
    font-family:'Orbitron',sans-serif; font-size:0.48rem; font-weight:700;
    letter-spacing:0.2em; padding:2px 8px;
    border:1px solid #4fc3f7; color:#4fc3f7; white-space:nowrap;
  }
  .divider { border:none; border-top:1px solid #1e1e2e; margin:0.75rem 0; }
  .section-header {
    font-family:'Orbitron',sans-serif; font-size:0.6rem; font-weight:700;
    color:#00e5ff; letter-spacing:0.25em; text-transform:uppercase;
    margin-bottom:0.5rem; margin-top:1.2rem;
  }
  .about-body { font-size:0.78rem; line-height:2.0; color:#adb1bc; }
  .about-body p { margin-bottom:0.9rem; }
  .highlight { color:#f5e642; }
  .statusbar {
    font-size:0.54rem; color:#2e3240; letter-spacing:0.16em;
    border-top:1px solid #181828; padding-top:0.55rem; margin-top:1.3rem;
    display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;
  }
</style></head><body>
<div class="viewer">
  <span class="corner tl">◤ ABOUT</span>
  <span class="corner tr">DOC//OPEN ◥</span>
  <span class="corner bl">◣ READ ONLY</span>
  <span class="corner br">ENC::NONE ◢</span>
  <div class="shard-id">SYS-DOC-000 &nbsp;&#9656;&nbsp; SYSTEM DOCUMENTATION</div>
  <div class="shard-title">
    About This Terminal
    <span class="badge">◆ VENDOR</span>
  </div>
  <hr class="divider"/>
  <div class="about-body">

    <div class="section-header">// USE-CASE</div>
    <p>The file contains several features that the developer has compiled together that resulted to this output.
    It features an <span class="highlight">Input Output</span>, <span class="highlight">Clickable elements</span>, and etc.
    And just to add the feel of security to it, the developer added a
    <span class="highlight">Login Process</span> that will give the user access to the content
    when the correct information was added and wont otherwise.</p>

    <div class="section-header">// TARGET USER</div>
    <p>Personally I don't put my aim on anyone except <span class="highlight">lore readers</span> and
    <span class="highlight">Cyberpunk players</span>, this is due to the fact that all of the content
    inside this file is all about the game.</p>

    <div class="section-header">// INPUT OUTPUT PROCESS</div>
    <p>Before accessing any shards, the user is greeted with a
    <span class="highlight">login screen</span>. You enter a handle and a passkey —
    get it right and the terminal opens up. Get it wrong and it tells you to try again.
    Simple as that.</p>

  </div>
  <div class="statusbar">
    <span>DOC VERSION: 1.0 &nbsp;|&nbsp; AUTHOR: LOUIS EMAN &nbsp;|&nbsp; CLEARANCE: OPEN</span>
    <span>⬡ NC-DATASHARD PROTOCOL // BY A&Ntilde;ON</span>
  </div>
</div>
</body></html>"""
    components.html(html, height=700, scrolling=True)


# this builds the entire screen and UI
def render_login_screen():

    ts = datetime.datetime.now().strftime("%Y.%m.%d // %H:%M:%S NST")


    _, col_mid, _ = st.columns([1, 1.4, 1])

    with col_mid:


        components.html(f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:#0a0a0e; font-family:'Share Tech Mono',monospace; padding:4px; }}
  .top-title {{
    font-family:'Orbitron',sans-serif; font-size:0.6rem; font-weight:900;
    letter-spacing:0.3em; color:#f5e642;
    text-align:center; padding:1.4rem 0 0.3rem;
  }}
  .top-ts {{
    font-size:0.44rem; color:#2a2f40; letter-spacing:0.14em;
    text-align:center; padding-bottom:1.2rem;
  }}
  .card {{
    background:#0d0d14; border:1px solid #1e1e2e; border-top:2px solid #f5e642;
    padding:1.6rem 2rem 1.4rem; position:relative;
    animation: flicker 9s infinite;
  }}
  @keyframes flicker {{
    0%,90%,95%,100% {{ opacity:1; }}
    91% {{ opacity:0.87; }}
    92% {{ opacity:1; }}
    93% {{ opacity:0.93; }}
  }}
  .corner {{ position:absolute; font-size:0.52rem; color:#f5e642; letter-spacing:0.15em; opacity:0.55; }}
  .tl {{ top:7px; left:10px; }}
  .tr {{ top:7px; right:10px; }}
  .card-id {{ font-size:0.56rem; color:#00e5ff; letter-spacing:0.3em; opacity:0.6; margin-top:0.4rem; margin-bottom:0.2rem; }}
  .card-title {{
    font-family:'Orbitron',sans-serif; font-size:0.9rem; font-weight:700;
    color:#f5e642; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.6rem;
  }}
  .divider {{ border:none; border-top:1px solid #1e1e2e; margin:0.6rem 0; }}
  .card-sub {{ font-size:0.62rem; color:#4a4f60; letter-spacing:0.14em; line-height:2.2; }}
</style></head><body>
  <div class="top-title">&#11041; &nbsp; NIGHT CITY // DATASHARD READER &nbsp; v2.4</div>
  <div class="top-ts">SYS:{ts} &nbsp; NODE::ACTIVE</div>
  <div class="card">
    <span class="corner tl">&#9700; AUTH</span>
    <span class="corner tr">TERMINAL &#9701;</span>
    <div class="card-id">SYS-AUTH-001 &nbsp;&#9656;&nbsp; ACCESS TERMINAL</div>
    <div class="card-title">IDENTITY VERIFICATION</div>
    <hr class="divider"/>
    <div class="card-sub">
      CLEARANCE REQUIRED TO ACCESS DATASHARD ARCHIVE<br/>
      SUBMIT HANDLE AND PASSKEY TO PROCEED
    </div>
  </div>
</body></html>""", height=255)


        handle  = st.text_input("HANDLE //", key="login_handle",
                                placeholder="enter handle...")
        passkey = st.text_input("PASSKEY //", key="login_passkey",
                                placeholder="enter passkey...", type="password")


        if st.session_state.auth_attempts > 0:
            st.markdown(f"""<div style="font-size:0.44rem;color:#ff1744;
                letter-spacing:0.14em;padding:0.2rem 0 0.1rem;opacity:0.8;">
                FAILED ATTEMPTS: {st.session_state.auth_attempts}</div>""",
                unsafe_allow_html=True)
            st.markdown("""<div style="font-size:0.42rem;color:#4a4f60;
                letter-spacing:0.14em;padding:0.1rem 0 0.2rem;">
                PSYCHOSIS INDEX</div>""", unsafe_allow_html=True)
            psychosis_level = min(st.session_state.auth_attempts / 5.0, 1.0)
            st.progress(psychosis_level)

        if st.button("⬡  AUTHENTICATE", key="auth_submit"):
            h = handle.strip().upper()
            p = passkey.strip()
            if h in VALID_CREDENTIALS and VALID_CREDENTIALS[h] == p:
                st.session_state.authenticated = True
                st.session_state.auth_attempts = 0
                st.rerun()
            else:
                st.session_state.auth_attempts += 1
                st.rerun()


        if st.session_state.auth_attempts > 0 and not st.session_state.authenticated:
            st.markdown("""<div style="font-size:0.52rem;color:#ff1744;
                letter-spacing:0.14em;padding:0.3rem 0.5rem;
                border-left:2px solid #ff1744;margin-top:0.3rem;">
                AUTH FAILED // TRY AGAIN</div>""", unsafe_allow_html=True)


        components.html("""<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
</head><body style="background:#0a0a0e;margin:0;padding:0;">
<div style="font-family:'Share Tech Mono',monospace;font-size:0.42rem;color:#1e2030;
  letter-spacing:0.14em;text-align:center;padding:0.8rem 0 0.4rem;line-height:2;">
  &#11041; DATASHARD MGMT SYS &nbsp;|&nbsp; BLACKWALL: STABLE &nbsp;|&nbsp; BY A&Ntilde;ON
</div>
</body></html>""", height=45)


# main is where everything actually runs — calls the bottom part of the file, enabling the login process and builds the UI
def main():
    load_global_css()


    # streamlit reruns the whole script on every single click
    # session_state remember things between reruns — otherwise everything would reset constantly to square one.
    if "cat" not in st.session_state:
        st.session_state.cat = "LORE"  # which category is open LORE or RECOVERED or CLASSIFIED
    if "idx" not in st.session_state:
        st.session_state.idx = 0  # which shard within that category is selected 

    if "panel_open" not in st.session_state:
        st.session_state.panel_open = True  # left panel starts open

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False  # not logged in by default

    if "auth_attempts" not in st.session_state:
        st.session_state.auth_attempts = 0  # tracks wrong password attempts for the psychosis bar
    if "cls_attempts" not in st.session_state:
        st.session_state.cls_attempts = 0

    if "active_section" not in st.session_state:
        st.session_state.active_section = "SHARDS"  # starts on the shard list, not the about page


    # if the user hasnt logged in yet, it will not continue it will stay here until user is logged in
    if not st.session_state.authenticated:
        render_login_screen()
        return

    ts = datetime.datetime.now().strftime("%Y.%m.%d // %H:%M:%S NST")

    # top bar — toggle button, rerun button, the big title, and the live timestamp
    col_s, col_r, col_t, col_sys = st.columns([1, 1, 6, 3])

    with col_s:

        if st.button("⬡  SHARDS", key="toggle_panel"):
            st.session_state.panel_open = not st.session_state.panel_open
            st.rerun()

    with col_r:

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


    # two-column layout — left is all the shards and on the right is the information 
    # when the panel is toggled off it disappears entirely, giving the viewer the full width
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


            # navigation buttons for shard and about
            nav_col1, nav_col2 = st.columns(2, gap="small")
            with nav_col1:
                if st.button("◈  SHARDS", key="nav_shards"):
                    st.session_state.active_section = "SHARDS"
                    st.rerun()
            with nav_col2:
                if st.button("◆  ABOUT", key="nav_about"):
                    st.session_state.active_section = "ABOUT"
                    st.rerun()

            st.markdown("<hr style='border-color:#111120;margin:0.4rem 0;'>",
                        unsafe_allow_html=True)


            # When reader is on the shards list, it shows the list and if on the about, only shows the about page
            # it swaps in between
            if st.session_state.active_section == "SHARDS":

                st.markdown("""<div style="font-family:'Orbitron',sans-serif;font-size:0.42rem;
                    letter-spacing:0.26em;color:#f5e642;opacity:0.7;
                    padding:0.5rem 0.4rem 0.2rem;">// LORE</div>""",
                    unsafe_allow_html=True)

                for i, s in enumerate(SHARDS["LORE"]):
                    active = st.session_state.cat == "LORE" and st.session_state.idx == i
                    label  = f"{'▶' if active else '·'} {s['id']}\n{s['title']}"
                    if st.button(label, key=f"lore_{i}"):

                        st.session_state.cat = "LORE"
                        st.session_state.idx = i
                        st.session_state.active_section = "SHARDS"
                        st.rerun()

                st.markdown("""<div style="font-family:'Orbitron',sans-serif;font-size:0.42rem;
                    letter-spacing:0.26em;color:#f5e642;opacity:0.7;
                    padding:0.5rem 0.4rem 0.2rem;margin-top:0.3rem;">// RECOVERED</div>""",
                    unsafe_allow_html=True)

                for i, s in enumerate(SHARDS["RECOVERED"]):
                    active = st.session_state.cat == "RECOVERED" and st.session_state.idx == i
                    label  = f"{'▶' if active else '·'} {s['id']}\n{s['title']}"
                    if st.button(label, key=f"rec_{i}"):

                        st.session_state.cat = "RECOVERED"
                        st.session_state.idx = i
                        st.session_state.active_section = "SHARDS"
                        st.rerun()


                # classified section header — Red = Locked, Green = Not Locked
                # same goes for the symbols :P
                cls_header_color = "#69f0ae" if st.session_state.get("cls_authenticated", False) else "#ff1744"
                cls_lock_symbol  = "◈" if st.session_state.get("cls_authenticated", False) else "⬡"
                cls_status_text  = "UNLOCKED" if st.session_state.get("cls_authenticated", False) else "LOCKED"

                st.markdown(f"""<div style="font-family:'Orbitron',sans-serif;font-size:0.42rem;
                    letter-spacing:0.26em;color:{cls_header_color};opacity:0.9;
                    padding:0.5rem 0.4rem 0.2rem;margin-top:0.3rem;">
                    {cls_lock_symbol} // CLASSIFIED [{cls_status_text}]</div>""",
                    unsafe_allow_html=True)

                for i, s in enumerate(LOCKED_SHARDS):
                    active = st.session_state.cat == "CLASSIFIED" and st.session_state.idx == i
                    if st.session_state.get("cls_authenticated", False):
                        label = f"{'▶' if active else '·'} {s['id']}\n{s['title']}"
                    else:
                        label = f"⬡ {s['id']}\n[ENCRYPTED]"
                    if st.button(label, key=f"cls_{i}"):
                        st.session_state.cat = "CLASSIFIED"
                        st.session_state.idx = i
                        st.session_state.active_section = "SHARDS"
                        st.rerun()

                st.markdown("<hr style='border-color:#111120;margin:0.6rem 0 0.4rem;'>",
                            unsafe_allow_html=True)

                # the classified access terminal — this separates them from other shards and 
                # the shards sits there doing nothing if the proper classification is true
                if not st.session_state.get("cls_authenticated", False):

                    st.markdown("""<div style="font-family:'Orbitron',sans-serif;font-size:0.44rem;
                        letter-spacing:0.22em;color:#ff1744;padding:0.3rem 0.4rem 0.15rem;">
                        ⬡ CLASSIFIED TERMINAL</div>""", unsafe_allow_html=True)

                    st.markdown("""<div style="font-size:0.42rem;color:#2e3240;
                        letter-spacing:0.12em;padding:0 0.4rem 0.35rem;line-height:1.9;">
                        HIGHER CLEARANCE REQUIRED<br/>SUBMIT CLASSIFIED CREDENTIALS</div>""",
                        unsafe_allow_html=True)

                    if st.session_state.cls_attempts > 0:
                        st.markdown(f"""<div style="font-size:0.42rem;color:#ff1744;
                            letter-spacing:0.12em;padding:0 0.4rem 0.2rem;opacity:0.75;">
                            FAILED ATTEMPTS: {st.session_state.cls_attempts}</div>""",
                            unsafe_allow_html=True)

                    cls_handle  = st.text_input("AGENT ID //",  key="cls_handle",
                                                placeholder="enter agent id...")
                    cls_passkey = st.text_input("CLEARANCE //", key="cls_passkey",
                                                placeholder="enter clearance code...", type="password")

                    if st.button("⬡  REQUEST CLEARANCE", key="cls_submit"):
                        ch = cls_handle.strip().upper()
                        cp = cls_passkey.strip()
                        if ch in CLASSIFIED_CREDENTIALS and CLASSIFIED_CREDENTIALS[ch] == cp:
                            st.session_state.cls_authenticated = True
                            st.session_state.cls_attempts = 0
                            st.rerun()
                        else:
                            st.session_state.cls_attempts += 1
                            st.rerun()

                    if st.session_state.cls_attempts > 0:
                        st.markdown("""<div style="font-size:0.5rem;color:#ff1744;
                            letter-spacing:0.12em;padding:0.25rem 0.4rem;
                            border-left:2px solid #ff1744;margin-top:0.2rem;">
                            CLEARANCE DENIED // TRY AGAIN</div>""", unsafe_allow_html=True)

                else:
                    # shows that the user has access to the encrypted file
                    st.markdown("""<div style="font-family:'Orbitron',sans-serif;font-size:0.44rem;
                        letter-spacing:0.22em;color:#69f0ae;padding:0.3rem 0.4rem 0.1rem;">
                        ◈ CLASSIFIED CLEARANCE ACTIVE</div>""", unsafe_allow_html=True)

                    st.markdown("""<div style="font-size:0.42rem;color:#4a4f60;
                        letter-spacing:0.12em;padding:0 0.4rem 0.35rem;line-height:2;">
                        CLEARANCE: OMEGA<br/>CLASSIFIED: UNLOCKED</div>""",
                        unsafe_allow_html=True)

                    if st.button("⟳  REVOKE CLEARANCE", key="cls_logout"):
                        # this only removes access to classified shards not the actual login
                        st.session_state.cls_authenticated = False
                        st.session_state.cls_attempts = 0
                        if st.session_state.cat == "CLASSIFIED":
                            st.session_state.cat = "LORE"
                            st.session_state.idx = 0
                        st.rerun()


            st.markdown("""<div style="font-size:0.44rem;color:#252535;letter-spacing:0.15em;
                line-height:2.2;padding:0.8rem 0.4rem;
                border-top:1px solid #111120;margin-top:0.8rem;">
                ⬡ DATASHARD MGMT SYS<br/>NODE STATUS: ONLINE<br/>
                BLACKWALL: STABLE<br/>CONNECTION: TUNNELED</div>""",
                unsafe_allow_html=True)


    # this focuses on what to display on the information cards or "shards"
    with col_viewer:
        if st.session_state.active_section == "ABOUT":
            render_about_page()
        elif st.session_state.cat == "CLASSIFIED":
            shard = LOCKED_SHARDS[st.session_state.idx]
            if st.session_state.get("cls_authenticated", False):
                render_shard_viewer(shard)
            else:
                render_locked_card(shard)
        else:
            shard = SHARDS[st.session_state.cat][st.session_state.idx]
            render_shard_viewer(shard)


# this one runs the actual code itself
if __name__ == "__main__":
    main()
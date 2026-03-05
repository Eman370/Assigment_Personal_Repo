import streamlit as sl

def boot_up():
    sl.set_page_config(page_title="NIGHT_CITY_HISTORY", layout="centered")
    
    visual = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&display=swap');

    .stApp {
        background: linear-gradient(90deg, #4A0404 0%, #B84528 50%, #D97B29 100%);
        background-attachment: fixed;
    }

    .terminal-window {
        font-family: 'Rajdhani', sans-serif;
        color: #ffffff;
        font-size: 1.25rem;
        line-height: 1.6;
        font-weight: 500;
        background: linear-gradient(90deg, rgba(217, 123, 41, 0.9) 0%, rgba(184, 69, 40, 0.9) 50%, rgba(74, 4, 4, 0.9) 100%);
        padding: 40px;
        border-radius: 4px;
        border-left: 5px solid #fcee0a;
        box-shadow: 15px 15px 30px rgba(0,0,0,0.5);
        max-height: 600px;
        overflow-y: auto;
        margin-top: 20px;
    }

    .terminal-window::-webkit-scrollbar { width: 8px; }
    .terminal-window::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.2); }
    .terminal-window::-webkit-scrollbar-thumb { background: #fcee0a; border-radius: 4px; }

    h1 {
        font-family: 'Rajdhani', sans-serif;
        font-weight: 700;
        color: #fcee0a !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        text-shadow: 3px 3px #000000;
        text-align: center;
    }
    
    .stRadio > label {
        font-family: 'Rajdhani', sans-serif;
        color: #ffffff !important;
        font-weight: 600;
        font-size: 1.1rem;
        text-transform: uppercase;
    }

    section[data-testid="stSidebar"] {
        background: rgba(0, 0, 0, 0.5) !important;
    }
    </style>
    """
    sl.markdown(visual, unsafe_allow_html=True)

def jack_in():
    boot_up()
    sl.title("DATA SHARD")
    
    dataShard = {
        "I. Origins & The Gang of Four": (
            "The Cyberpunk universe timeline diverges from real history in the late 1980s. Political instability and "
            "economic collapse began reshaping global society as megacorporations grew into entities more powerful than "
            "entire nations. In the United States, a shadow political alliance known as the 'Gang of Four'—consisting of "
            "the President, the CIA Director, the NSA Director, and the Secretary of Defense—quietly manipulated national "
            "policy. Economic inequality rapidly expanded, unemployment skyrocketed, and millions were pushed into poverty. "
            "During this period, technological development accelerated dramatically, especially in cybernetics and the NET. "
            "The United States became involved in the Central American Wars, fought largely through corporate military contractors. "
            "Many soldiers returned with advanced cybernetic replacements, but struggled to reintegrate into a collapsing "
            "society. By the late 1990s, the world was a powder keg of corporate greed and technological obsession."
        ),
        "II. The Rise of Night City": (
            "In 1994, an idealistic entrepreneur named Richard Night envisioned a technological utopia along the California coast. "
            "Originally named Coronado City, it was intended to be free from corporate and government interference. However, "
            "the project required massive corporate funding. Night was assassinated in 1998, likely by the mob or corporate rivals. "
            "The city was renamed 'Night City' in his honor, but it quickly devolved into a battleground for gangs and "
            "corporate interests. The 'Mob Era' saw organized crime take control until the megacorporations—led by Arasaka—"
            "launched a violent cleansing of the city's leadership to install their own order. This set the stage for the "
            "corporate-dominated metropolis seen in the decades to come."
        ),
        "III. The 4th Corporate War": (
            "The early 2020s were defined by the Fourth Corporate War, a global conflict between CINO and OTEC that escalated "
            "when the world's two largest military corporations, Arasaka and Militech, took sides. This wasn't just a trade "
            "dispute; it was total war. Global supply chains collapsed, and the legendary netrunner Rache Bartmoss released "
            "the 'DataKrash' virus, shattering the NET and releasing rogue AIs. The war reached its horrific climax in 2023 "
            "at the Arasaka Tower in Night City. A strike team including Johnny Silverhand and Morgan Blackhand detonated "
            "a suitcase nuke to destroy the Arasaka database. The resulting blast leveled the city center and killed "
            "over half a million people, marking the end of the Corporate Era and the beginning of the Red."
        ),
        "IV. Time of the Red & The Blackwall": (
            "Following the 2023 explosion, atmospheric pollution from the debris and nuclear fallout turned the skies a "
            "permanent, haunting crimson—giving this era the name 'The Time of the Red.' For decades, the world was "
            "fragmented. The old NET was a wasteland of killer AIs. To protect what remained of human technology, "
            "NetWatch and rogue AIs collaborated to construct the 'Blackwall.' This massive digital barrier serves as "
            "the only thing standing between humanity and the machine-gods beyond. During this period, Night City was "
            "rebuilt from the ashes, and the Nomad clans became the primary traders in a world where traditional "
            "shipping was no longer safe. Technology became more localized, rugged, and survival-oriented."
        ),
        "V. The 2070s & Phantom Liberty": (
            "By the 2070s, Arasaka had returned to Night City, and the Unification War had left the NUSA fractured. "
            "In 2077, the mercenary V became a catalyst for change after stealing the 'Relic' from Arasaka. During the "
            "same period, the 'Phantom Liberty' events unfolded in Dogtown—a militarized district controlled by warlord "
            "Kurt Hansen. President Rosalind Myers crash-landed in this lawless zone, sparking a covert espionage war "
            "involving agents Solomon Reed and Songbird. Songbird, a netrunner forced to touch the Blackwall, represented "
            "the ultimate danger of the era: the thin line between human consciousness and rogue AI invasion. V's journey "
            "through these events marked the most recent point in the official timeline, where the fate of the city and "
            "the soul itself remained in the balance."
        )
    }

    indices = [k for k in dataShard]
    input_signal = sl.sidebar.radio("HISTORY_LOG_ACCESS:", indices)
    
    sl.markdown(f'<div class="terminal-window">{dataShard[input_signal]}</div>', unsafe_allow_html=True)
    
    sl.caption("CONNECTION: TUNNELED // RAJDHANI_SANS // BY AÑON")

if __name__ == "__main__":
    jack_in()
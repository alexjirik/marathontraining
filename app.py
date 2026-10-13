import streamlit as st

# Set to "wide" mode so the calendar stretches horizontally across the screen
st.set_page_config(page_title="Marathon Training Plan", page_icon="🏃", layout="wide")

st.title("📅 Weekly Training Calendar")
st.markdown("Your hybrid marathon training plan focusing on injury prevention, Solidcore, and aerobic base building.")
st.divider()

# Create a 7-column layout for the week
days = st.columns(7)

# --- MONDAY ---
with days[0]:
    st.subheader("Mon")
    st.info("💪 Solidcore")
    with st.expander("Workout Details"):
        st.write("**Focus:** Core & Muscular Endurance")
        st.write("No running today. Protect your legs and build that stability.")
    st.checkbox("Complete", key="mon")

# --- TUESDAY ---
with days[1]:
    st.subheader("Tue")
    st.success("👟 3-4 mi Run")
    with st.expander("Warm-Up (5 min)"):
        st.write("• Leg Swings (10/leg)\n• Open Gate (10)\n• Toy Soldier (10/leg)\n• Hamstring Sweeps (8/leg)\n• Walking Lunges (10 total)\n• High Knees (20s)")
    with st.expander("Run Details"):
        st.write("**Pace:** Strictly conversational.")
        st.write("**Cool Down:** Foam roll hip flexors & quads.")
    st.checkbox("Complete", key="tue")

# --- WEDNESDAY ---
with days[2]:
    st.subheader("Wed")
    st.info("💪 Solidcore")
    with st.expander("Workout Details"):
        st.write("**Focus:** Deep core engagement.")
        st.write("Fuel well today to prep your legs for tomorrow's run.")
    st.checkbox("Complete", key="wed")

# --- THURSDAY ---
with days[3]:
    st.subheader("Thu")
    st.success("👟 4-5 mi Run")
    with st.expander("Warm-Up (5 min)"):
        st.write("Complete the same 6-move dynamic warm-up as Tuesday.")
    with st.expander("Run Details"):
        st.write("**Pace:** Strictly conversational.")
    with st.expander("Post-Run Prehab"):
        st.write("• Calf Raise (3x15)\n• Tibialis Raise (3x20)\n• Banded Walk (3x10/way)")
    st.checkbox("Complete", key="thu")

# --- FRIDAY ---
with days[4]:
    st.subheader("Fri")
    st.warning("🚴 Aerobic Flush")
    with st.expander("Workout Details"):
        st.write("**Time:** 35–45 mins")
        st.write("**Mode:** Cycling, Swimming, or Elliptical")
        st.write("**Focus:** Zone 2 low-impact recovery. Push blood through the legs without joint impact.")
    st.checkbox("Complete", key="fri")

# --- SATURDAY ---
with days[5]:
    st.subheader("Sat")
    st.error("🔥 Long Run")
    with st.expander("Run Details"):
        st.write("**Distance:** 6+ miles")
        st.write("Start at 6 mi, add 1 mi every two weeks.")
        st.write("Do your dynamic warm-up first. Stretch calves/hamstrings after.")
    st.checkbox("Complete", key="sat")

# --- SUNDAY ---
with days[6]:
    st.subheader("Sun")
    st.markdown("💤 **Full Rest**")
    with st.expander("Recovery Details"):
        st.write("Full recovery today.")
        st.write("Light walking or mobility is okay, but zero structured exercise. Let your body absorb the week's work.")
    st.checkbox("Complete", key="sun")

st.divider()

# Check if all days are marked complete to trigger balloons!
if all([st.session_state.get(k, False) for k in ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]]):
    st.success("🎉 Incredible job! You crushed the entire week of training!")
    st.balloons()

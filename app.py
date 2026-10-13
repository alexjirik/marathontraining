import streamlit as st

# Configure the page
st.set_page_config(page_title="Marathon Training Plan", page_icon="🏃", layout="centered")

st.title("🏃 Custom Marathon Training Plan")
st.markdown("Your hybrid marathon training plan focusing on injury prevention, Solidcore, and aerobic base building.")
st.divider()

# Monday
st.header("Monday: Solidcore")
st.info("💪 Core & Muscular Endurance (No Impact)")
with st.expander("View Details"):
    st.markdown("""
    * **Workout:** Solidcore class
    * **Focus:** Muscular endurance, core control, and pelvic stability. 
    * **Note:** No running today. Protect your legs.
    """)
st.checkbox("Mark Monday Complete", key="mon")
st.divider()

# Tuesday
st.header("Tuesday: Easy Run (3–4 miles)")
st.success("👟 Easy Conversational Pace")
with st.expander("Pre-Run Warm-Up (5 min)"):
    st.markdown("""
    * **Forward Leg Swings:** 10 reps per leg
    * **Open the Gate:** 10 reps alternating
    * **Toy Soldier Walk:** 10 steps per leg
    * **Hamstring Sweeps:** 8 reps per leg
    * **Walking Lunges:** 10 steps total
    * **High Knees:** 20 seconds
    """)
with st.expander("Run Details & Cool Down"):
    st.markdown("""
    * **Run:** 3–4 miles at a strictly conversational, easy pace.
    * **Cool Down:** 3–5 minutes foam rolling your hip flexors and quads (crucial after Monday's Solidcore).
    """)
st.checkbox("Mark Tuesday Complete", key="tue")
st.divider()

# Wednesday
st.header("Wednesday: Solidcore")
st.info("💪 Deep Core Engagement")
with st.expander("View Details"):
    st.markdown("""
    * **Workout:** Solidcore class
    * **Focus:** Deep core engagement. Fuel well today to prep your legs for tomorrow.
    """)
st.checkbox("Mark Wednesday Complete", key="wed")
st.divider()

# Thursday
st.header("Thursday: Easy Run (4–5 miles) + Prehab")
st.success("👟 Base Building + Tendon Health")
with st.expander("Pre-Run Warm-Up (5 min)"):
    st.markdown("Complete the same 6-move dynamic warm-up sequence as Tuesday.")
with st.expander("Run Details"):
    st.markdown("* **Run:** 4–5 miles at a strictly conversational pace.")
with st.expander("Post-Run Lower Leg Prehab"):
    st.markdown("""
    * **Standing Calf Raise:** 3 sets x 12-15 reps
    * **Tibialis Wall Raise:** 3 sets x 15-20 reps
    * **Banded Monster Walk:** 3 sets x 10 steps each way
    * **Cool Down:** 3–5 minutes foam rolling your hip flexors and quads.
    """)
st.checkbox("Mark Thursday Complete", key="thu")
st.divider()

# Friday
st.header("Friday: Aerobic Flush")
st.warning("🚴 Low-Impact Active Recovery")
with st.expander("View Details"):
    st.markdown("""
    * **Workout:** 35–45 minutes of Cycling (85-95 RPM), Freestyle Swimming, or Elliptical.
    * **Focus:** Keep resistance light. This is a Zone 2 "flush" session to push blood through your legs and clear metabolic waste without any joint impact.
    """)
st.checkbox("Mark Friday Complete", key="fri")
st.divider()

# Saturday
st.header("Saturday: Long Run")
st.error("🔥 Endurance Builder (6+ miles)")
with st.expander("Run Details & Progression"):
    st.markdown("""
    * **Warm-up:** Complete the 6-move dynamic warm-up sequence before stepping onto the road.
    * **Run:** Start at 6 miles. Add 1 mile every two weeks. Maintain an easy, breathable pace.
    * **Cool Down:** Walk for 5-10 minutes immediately after, followed by gentle static stretching for calves, hamstrings, and quads.
    """)
st.checkbox("Mark Saturday Complete", key="sat")
st.divider()

# Sunday
st.header("Sunday: Full Rest")
st.markdown("💤 **Recovery Day**")
with st.expander("View Details"):
    st.markdown("""
    * **Workout:** Complete rest.
    * **Focus:** Light walking or gentle mobility work is fine, but zero structured exercise. Let your bones, tendons, and muscles absorb the week's training.
    """)
st.checkbox("Mark Sunday Complete", key="sun")

st.balloons() if all([st.session_state.get(k, False) for k in ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]]) else None

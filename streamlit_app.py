import pandas as pd
import streamlit as st
import plotly.express as px

ph_values = {
    "Apple, baked with sugar": "3.20 - 3.55",
    "Apple, eating": "3.30-4.00",
    "Apple - Delicious": 3.9,
    "Apple - Golden Delicious": 3.6,
    "Apple - Jonathan": 3.33,
    "Apple - McIntosh": 3.34,
    "Apple Juice": "3.35-4.00",
    "Apple Sauce": "3.10-3.60",
    "Apple - Winesap": 3.47,
    "Apricots": "3.30-4.80",
    "Apricot nectar": 3.78,
    "Apricots, pureed": "3.42-3.83",
    "Artichokes": "5.50-6.00",
    "Artichokes, canned, acidified": "4.30-4.60",
    "Artichokes, Jerusalem, cooked": "5.93-6.00",
    "Asparagus": "6.00-6.70",
    "Avocados": "6.27-6.58",
    "Baby corn": 5.20,
    "Bamboo Shoots": "5.10-6.20",
    "Bananas": "4.50-5.20",
    "Beans": "5.60-6.50",
    "Beans, black": "5.78-6.02",
    "Beans, kidney": "5.40-6.00",
    "Beans, lima": 6.50,
    "Beans, soy": "6.00-6.60",
    "Beans, string": 5.60,
    "Beans, wax": "5.30-5.70",
    "Beans, pork & tomato sauce": "5.10-5.80",
    "Beets": "5.30-6.60",
    "Beets, canned, acidified": "4.30-4.60",
    "Blackberries, Washington": "3.85-4.50",
    "Blueberries, Maine": "3.12-3.33",
    "Blueberries, frozen": "3.11-3.22",
    "Broccoli": "6.30-6.85",
    "Brussels sprout": "6.00-6.30",
    "Cabbage": "5.20-6.80",
    "Cabbage, green": "5.50-6.75",
    "Cactus": 4.70,
    "Cantaloupe": "6.13-6.58",
    "Carrots": "5.88-6.40",
    "Cauliflower": 5.6,
    "Celery": "5.70-6.00",
    "Cherries, California": "4.01-4.54",
    "Cherries, red, water pack": "3.25-3.82",
    "Cherries, Royal Ann": "3.80-3.83",
    "Corn": "5.90-7.50",
    "Cucumbers": "5.12-5.78",
    "Cucumbers, dill pickles": "3.20-3.70",
    "Cucumbers, pickled": "4.20-4.60",
    "Eggplant": "4.5-5.3",
    "Figs, Calamyrna": "5.05-5.98",
    "Four bean salad": 5.60,
    "Fruit cocktail": "3.60-4.00",
    "Grapes, Concord": "2.80-3.00",
    "Grapes, Niagara": "2.80-3.27",
    "Grapes, seedless": "2.90-3.82",
    "Grapefruit": "3.00-3.75",
    "Horseradish, ground": 5.35,
    "Jam, fruit": "3.50-4.50",
    "Jellies, fruit": "3.00-3.50",
    "Ketchup": "3.89-3.92",
    "Leeks": "5.50-6.17",
    "Lemon juice": "2.00-2.60",
    "Lime juice": "2.00-2.35",
    "Lime": "2.00-2.80",
    "Loganberries": "2.70-3.50",
    "Mangoes, ripe": "5.80-6.00",
    "Mangoes, green": "3.40-4.80",
    "Maple syrup": "6.00-6.67",
    "Melon, Honey dew": 5.15,
    "Mint jelly": 3.01,
    "Mushrooms": "6.00-6.70",
    "Nectarines": "3.92-4.18",
    "Okra, cooked": "5.50-6.60",
    "Olives, black": "6.00-7.00",
    "Olives, green fermented": "3.60-4.60",
    "Olives, ripe": "6.00-7.50",
    "Onions, pickled": "3.70-4.60",
    "Onions, red": "5.30-5.880",
    "Onions, white": "5.37-5.85",
    "Onions, yellow": "5.32-5.60",
    "Oranges, Florida": "3.69-4.34",
    "Orange juice, California": "3.30-4.19",
    "Orange juice, Florida": "3.30-4.15",
    "Palm, heart of": 6.70,
    "Papaya": "5.20-6.00",
    "Parsnip": "5.30-5.70",
    "Peaches": "3.30-4.05",
    "Pears, Bartlett": "3.50-4.60",
    "Peas, canned": "5.70-6.00",
    "Peas, Garbanzo": "6.48-6.80",
    "Peppers": "4.65-5.45",
    "Peppers, green": "5.20-5.93",
    "Persimmons": "4.42-4.70",
    "Pickles, fresh pack": "5.10-5.40",
    "Pimiento": "4.40-4.90",
    "Pineapple": "3.20-4.00",
    "Plums, Blue": "2.80-3.40",
    "Plums, Red": "3.60-4.30",
    "Pomegranate": "2.93-3.20",
    "Potatoes": "5.40-5.90",
    "Prunes": "3.63-3.92",
    "Pumpkin": "4.990-5.50",
    "Radishes, red": "5.85-6.05",
    "Radishes, white": "5.52-5.69",
    "Raspberries": "3.22-3.95",
    "Rhubarb": "3.10-3.40",
    "Sauerkraut": "3.30-3.60",
    "Spinach": "5.50-6.80",
    "Squash, acorn, cooked": "5.18-6.49",
    "Squash, white, cooked": "5.52-5.80",
    "Squash, yellow, cooked": "5.79-6.00",
    "Strawberries": "3.00-3.90",
    "Sweet potatoes": "5.30-5.60",
    "Three-bean salad": 5.40,
    "Tofu (soybean curd)": 7.20,
    "Tomatillo": 3.83,
    "Tomatoes": "4.30-4.90",
    "Tomatoes, juice": "4.10-4.60",
    "Tomatoes, paste": "3.50-4.70",
    "Tomatoes, puree": "4.30-4.47",
    "Tomatoes, vine ripened": "4.42-4.65",
    "Vinegar": "2.40-3.40",
    "Vinegar, cider": 3.10,
    "Watermelon": "5.18-5.60",
    "Zucchini, cooked": "5.69-6.10",
    "Butter": "6.1-6.4",
    "Corn starch": "4.0-7.0",
    "Corn syrup": 5.0,
    "Honey": 3.9,
    "Molasses": "5.0-5.5",
    "Sugar": "5.0-6.0",
    "Flour": "6.0-6.3",
}

path = "iupac_high-confidence_v2_2.csv"
data = pd.read_csv(path)

data["pka_value"] = pd.to_numeric(data["pka_value"], errors="coerce")
data = data.dropna(subset=["pka_value"])

st.title("Exploring Acidity and Basicity in Everyday Foods")

st.header("Data Overview")
st.markdown("**Title:** Heatmap of pKa Values for Edible Compounds")
st.markdown(
    "**Caption:** Heatmap showing the density of pKa values for a dataset of edible compounds. This visualization helps to identify areas with higher concentrations of pKa values."
)

fig1 = px.density_heatmap(
    data,
    x="pka_value",
    nbinsx=100,  # Increased number of bins for better granularity
    title="Heatmap of pKa Values in Foods",
    color_continuous_scale=px.colors.sequential.Plasma,  # Changed color scale for better contrast
)

fig1.update_layout(
    xaxis_title="pKa Value",
    yaxis_title="Density",
    margin=dict(l=40, r=40, t=40, b=40),
    coloraxis_colorbar=dict(
        title="Density", tickvals=[0, 0.2, 0.4, 0.6, 0.8, 1], ticktext=["Low"]
    ),
)

st.plotly_chart(fig1)

st.header("Graph 1: pKa Distribution of Foods")
st.markdown("**Title:** Distribution of pKa Values for Edible Compounds")
st.markdown(
    "**Caption:** Histogram depicting the frequency distribution of pKa values for a dataset of edible compounds. A higher pKa indicates a weaker acid and a stronger conjugate base. This distribution reveals the range of acidic strengths present in common food items."
)
fig1 = px.histogram(
    data, x="pka_value", nbins=50, title="Distribution of pKa Values in Foods"
)
fig1.update_layout(xaxis_title="pKa Value", yaxis_title="Count")
st.plotly_chart(fig1)

st.header("Graph 2: pKa vs Acidity Label")
st.markdown("**Title:** pKa Values Categorized by Acidity Label")
st.markdown(
    "**Caption:** Box plot illustrating the relationship between assigned acidity labels and pKa values. The boxes represent the interquartile range (IQR), the whiskers extend to 1.5 times the IQR, and outliers are plotted individually. This visualization allows for comparison of pKa distributions across different acidity classifications."
)
fig2 = px.box(
    data, x="acidity_label", y="pka_value", title="pKa Values by Acidity Label"
)
fig2.update_layout(xaxis_title="Acidity Label", yaxis_title="pKa Value")
st.plotly_chart(fig2)

st.header("Graph 3: Interactive Scatter Plot of pKa Values")
st.markdown("**Title:** pKa Values of Food Constituents")
st.markdown(
    "**Caption:** Interactive scatter plot displaying the pKa values of various food constituents, colored by their acidity label. Hovering over a point reveals the specific food item. This interactive visualization allows exploration of the relationship between food type and pKa."
)
fig3 = px.scatter(
    data,
    x="name_contributors",
    y="pka_value",
    color="acidity_label",
    hover_name="name_contributors",
    title="pKa Values of Different Foods",
)
fig3.update_layout(xaxis_title="Food", yaxis_title="pKa Value")
st.plotly_chart(fig3)

st.header("Interactive Element: Filter Foods by pKa Range")
pka_min = st.slider(
    "Minimum pKa",
    min_value=float(data["pka_value"].min()),
    max_value=float(data["pka_value"].max()),
    value=float(data["pka_value"].min()),
)
pka_max = st.slider(
    "Maximum pKa",
    min_value=float(data["pka_value"].min()),
    max_value=float(data["pka_value"].max()),
    value=float(data["pka_value"].max()),
)
filtered_data = data[(data["pka_value"] >= pka_min) & (data["pka_value"] <= pka_max)]
st.markdown("**Title:** Food Constituents within Selected pKa Range")
st.markdown(
    "**Caption:** Table displaying the food constituents whose pKa values fall within the user-specified range. This table provides a detailed view of the filtered data, including the name, pKa value, and acidity label of each constituent."
)
st.write(filtered_data)

st.header("Graph 4: Filtered pKa Distribution")
st.markdown("**Title:** Distribution of pKa Values for Selected Food Constituents")
st.markdown(
    "**Caption:** Histogram representing the frequency distribution of pKa values after filtering the dataset based on a user-defined pKa range. This visualization allows for a focused analysis of pKa distributions within a specific range of interest."
)
fig4 = px.histogram(
    filtered_data,
    x="pka_value",
    nbins=50,
    title="Filtered Distribution of pKa Values in Foods",
)
fig4.update_layout(xaxis_title="pKa Value", yaxis_title="Count")
st.plotly_chart(fig4)

ph_values_list = []
for item, ph_range in ph_values.items():
    if isinstance(ph_range, str) and "-" in ph_range:
        ph_min, ph_max = map(float, ph_range.split("-"))
    else:
        ph_min = ph_max = float(ph_range)
    ph_values_list.append({"Item": item, "pH Min": ph_min, "pH Max": ph_max})

df = pd.DataFrame(ph_values_list, columns=["Item", "pH Min", "pH Max"])

st.title("Everyday Foods: Acids, Bases, and Your Teeth")
st.markdown(
    "This interactive website delves into the hidden chemical world of our everyday meals, exploring the fundamental concepts of acidity and basicity, their interaction with our bodies (specifically teeth), and how we combat their effects."
)

st.header("The Acid-Base Spectrum of Food")
st.subheader("1: pH Scale of Common Foods")
st.markdown("**Title:** pH Ranges of Common Foods")
st.markdown(
    "**Caption:** Interactive scatter plot showcasing the pH ranges of common food items. The vertical bars represent the range between minimum and maximum pH values for each food. The size and color of the markers are scaled according to the maximum pH value."
)
df["pH Mid"] = (df["pH Min"] + df["pH Max"]) / 2
fig1 = px.scatter(
    df,
    x="Item",
    y="pH Mid",
    error_y=df["pH Max"] - df["pH Mid"],
    error_y_minus=df["pH Mid"] - df["pH Min"],
    size="pH Max",
    color="pH Mid",
    hover_name="Item",
    title="pH Range of Different Items",
    labels={"pH Mid": "pH Value"},
    color_continuous_scale=px.colors.sequential.Viridis,
)
fig1.update_layout(
    xaxis_title="Food Item",
    yaxis_title="pH Value",
    xaxis_tickangle=-45,
    height=600,
    margin=dict(l=40, r=40, t=40, b=150),
    hovermode="closest",
)
fig1.update_coloraxes(colorbar_title="pH Value")
st.plotly_chart(fig1)

st.header("The Chemistry of Acids and Bases")
st.subheader("2: Dissociation of Acids and Bases")
st.markdown("**Title:** Acid-Base Dissociation Equilibria")
st.markdown(
    "**Caption:** These equations illustrate the equilibrium reactions for the dissociation of a generic acid (HA) and a generic base (B) in aqueous solution. The equilibrium constant for the autoionization of water (Kw) is defined as [H+][OH-] and is equal to 1.0 x 10⁻¹⁴ at 25°C."
)
st.latex(r"HA \, (acid) \, \rightleftharpoons \, H^+ + A^- \, (conjugate \, base)")
st.latex(
    r"B \, (base) + H_2O \, \rightleftharpoons \, BH^+ \, (conjugate \, acid) + OH^-"
)

st.header("The Assault on Teeth")
st.subheader("3: Demineralization of Teeth")
st.markdown(
    "**Title:** Potential for Tooth Demineralization by Common Foods (pH < 5.5)"
)
st.markdown(
    "**Caption:** Interactive scatter plot highlighting the pH ranges of food items with pH values below 5.5, a threshold below which significant demineralization of tooth enamel can occur. The data visualization aids in understanding the potential erosive effects of acidic foods on tooth structure."
)

df_filtered = df[df["pH Min"] < 5.5]
df_filtered["pH Mid"] = (df_filtered["pH Min"] + df_filtered["pH Max"]) / 2

fig2 = px.scatter(
    df_filtered,
    x="Item",
    y="pH Mid",
    error_y=df_filtered["pH Max"] - df_filtered["pH Mid"],
    error_y_minus=df_filtered["pH Mid"] - df_filtered["pH Min"],
    size="pH Max",
    color="pH Mid",
    hover_name="Item",
    title="Demineralization of Teeth",
    labels={"pH Mid": "pH Value"},
    color_continuous_scale=px.colors.sequential.Viridis,
)

fig2.add_shape(
    type="line",
    x0=0,
    y0=5.5,
    x1=1,
    y1=5.5,
    xref="paper",
    yref="y",
    line=dict(color="Red", width=2, dash="dash"),
)

fig2.add_annotation(
    x=0.5,
    y=5.5,
    xref="paper",
    yref="y",
    text="Critical pH Threshold (5.5)",
    showarrow=False,
    font=dict(size=12, color="Red"),
)

fig2.update_layout(
    xaxis_title="Food Item",
    yaxis_title="pH Value",
    xaxis_tickangle=-45,
    height=600,
    margin=dict(l=40, r=40, t=40, b=150),
    hovermode="closest",
)
fig2.update_coloraxes(colorbar_title="pH Value")

st.plotly_chart(fig2)

st.header("Defense Mechanisms: Saliva and Toothpaste")
st.subheader("4: Buffering Action of Saliva")
st.markdown("**Title:** Bicarbonate Buffering System in Saliva")
st.markdown(
    "**Caption:** The equation describes the equilibrium reaction involving bicarbonate (HCO₃⁻), a key component of saliva's buffering system, which helps neutralize acids and maintain oral pH homeostasis."
)
st.latex(
    r"H^+ + HCO_3^- \, \rightleftharpoons \, H_2CO_3 \, \rightleftharpoons \, H_2O + CO_2"
)

st.subheader("5: Chemical Composition of Toothpaste")
st.markdown("**Title:** Fluorapatite Formation in Tooth Enamel")
st.markdown(
    "**Caption:** The equation illustrates the reaction of fluoride ions (F⁻) with hydroxyapatite in tooth enamel, forming fluorapatite. This process strengthens tooth structure and enhances resistance to acid-induced demineralization."
)
st.header("Defense Mechanisms: Saliva and Toothpaste")
st.subheader("4: Buffering Action of Saliva")


st.markdown("**Title:** Bicarbonate Buffering System in Saliva")
st.markdown(
    "**Caption:** The equation describes the equilibrium reaction involving bicarbonate (HCO₃⁻), a key component of saliva's buffering system, which helps neutralize acids and maintain oral pH homeostasis."
)
st.latex(
    r"H^+ + HCO_3^- \, \rightleftharpoons \, H_2CO_3 \, \rightleftharpoons \, H_2O + CO_2"
)

st.subheader("5: Chemical Composition of Toothpaste")
st.markdown("**Title:** Fluorapatite Formation in Tooth Enamel")
st.markdown(
    "**Caption:** The equation illustrates the reaction of fluoride ions (F⁻) with hydroxyapatite in tooth enamel to form fluorapatite, which is more resistant to acid attack."
)
st.latex(r"Ca_5(PO_4)_3OH + F^- \, \rightleftharpoons \, Ca_5(PO_4)_3F + OH^-")

st.header("Conclusion")
st.markdown(
    "In this website I have attempted to explore the acidity and basicity of common foods, their impact on dental health, along with the body's natural defense mechanisms. For me, understanding the chemical properties of the foods I consume, has helped me to make informed choices to protect my teeth and overall health. though I must admit it was more just beacuse I like messing around with python."
)
st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2dubnAxMGcwN2ozazJzY2pvazhyM2R0Zm5hdDhjdzI2NzYwaDFqYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NGIBa8a9KWzoFxW1c8/giphy.webp", caption="This is me right now, I dident send the email and it was sitting in my drafts.")

ascii_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀____
　　　　　／＞　　フ
　　　　　| 　_　 _ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　|　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿ヽ)__) __)
　＼二つ
"""

st.text(ascii_art)
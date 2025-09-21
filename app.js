const askBtn = document.getElementById('ask');
const qEl = document.getElementById('q');
const ansEl = document.getElementById('ans');
const webEl = document.getElementById('use_web');
const chipsEl = document.getElementById('chips');

const TRY_QUERIES = [
  "show the employment rate trend for diploma graduates since 2016",
  "which state had the highest mean salary last year?",
  "compare unemployment rate between Sabah and Sarawak in 2020–2023",
  "top 3 industries by graduates in 2022",
  "forecast employed_total for the next 3 years"
];

function renderChips() {
  chipsEl.innerHTML = "";
  TRY_QUERIES.forEach(q => {
    const s = document.createElement("span");
    s.className = "chip"; s.textContent = q;
    s.onclick = () => { qEl.value = q; askBtn.click(); };
    chipsEl.appendChild(s);
  });
}
renderChips();

askBtn.onclick = async () => {
  ansEl.textContent = "Thinking…";
  const body = { message: qEl.value, use_web: webEl.checked };
  const r = await fetch("http://127.0.0.1:8000/chat/chat/", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify(body)
  });
  const j = await r.json();
  ansEl.innerHTML = (j.answer || "(no answer)");
};

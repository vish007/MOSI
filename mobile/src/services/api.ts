const API = process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8000';

export async function runDemoFlow() {
  const res = await fetch(`${API}/flow/demo`, { method: 'POST' });
  return res.json();
}

export async function submitFeedback(payload: Record<string, string>) {
  const res = await fetch(`${API}/feedback`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  return res.json();
}

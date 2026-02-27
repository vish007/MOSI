import React, { useState } from 'react';
import { SafeAreaView, ScrollView, Text, Button, View } from 'react-native';
import { runDemoFlow, submitFeedback } from './src/services/api';

export default function App() {
  const [flow, setFlow] = useState<any>(null);

  const load = async () => {
    const data = await runDemoFlow();
    setFlow(data);
  };

  const feedback = async (rating: string) => {
    if (!flow?.signal) return;
    await submitFeedback({
      user_id: flow.login.user.id,
      symbol: flow.signal.symbol,
      signal_id: 'signal-001',
      rating,
      comment: 'Looks useful'
    });
  };

  return (
    <SafeAreaView>
      <ScrollView contentContainerStyle={{ padding: 16, gap: 12 }}>
        <Text style={{ fontSize: 24, fontWeight: '700' }}>MOSI</Text>
        <Text>1) Link broker → 2) Sync portfolio → 3) Generate signal + SHAP → 4) Record feedback</Text>
        <Button title="Run MOSI Flow" onPress={load} />
        {flow && (
          <View style={{ gap: 8 }}>
            <Text>Broker: {flow.broker.provider} linked ✅</Text>
            <Text>Holdings Synced: {flow.portfolio.holdings.length}</Text>
            <Text>Signal: {flow.signal.signal} ({flow.signal.confidence})</Text>
            <Text>{flow.signal.explanation.english_explanation}</Text>
            <Button title="👍 Helpful" onPress={() => feedback('up')} />
            <Button title="👎 Not Helpful" onPress={() => feedback('down')} />
          </View>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

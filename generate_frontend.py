import os

base = r"C:\Users\LENOVO\OneDrive\Desktop\agent bazar\frontend"

files = {
    "app/globals.css": """
@import "tailwindcss";

@theme {
  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-display: "Space Grotesk", ui-sans-serif, system-ui, sans-serif;

  --color-indigo-900: #312e81;
  --color-indigo-600: #4f46e5;
  --color-indigo-400: #818cf8;
  
  --color-slate-900: #0f172a;
  --color-slate-800: #1e293b;
  --color-slate-100: #f1f5f9;
  
  --color-background: var(--color-slate-900);
  --color-foreground: var(--color-slate-100);
}

body {
  background-color: var(--color-background);
  color: var(--color-foreground);
  font-family: var(--font-sans);
}
    """,
    "app/layout.tsx": """
import type { Metadata } from "next";
import { Inter, Space_Grotesk } from "next/font/google";
import "./globals.css";
import { Toaster } from "sonner";

const inter = Inter({ subsets: ["latin"], variable: "--font-sans" });
const space = Space_Grotesk({ subsets: ["latin"], variable: "--font-display" });

export const metadata: Metadata = {
  title: "AgentBazaar",
  description: "Decentralized marketplace for autonomous AI agents",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.variable} ${space.variable} font-sans antialiased bg-slate-900 text-slate-100`}>
        <nav className="border-b border-slate-800 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex items-center justify-between h-16">
              <div className="flex items-center gap-2">
                <span className="font-display font-bold text-xl text-indigo-400 tracking-tight">AgentBazaar</span>
              </div>
              <div className="flex gap-4">
                <a href="/" className="text-sm font-medium hover:text-indigo-400 transition-colors">Marketplace</a>
                <a href="/dashboard" className="text-sm font-medium hover:text-indigo-400 transition-colors">Dashboard</a>
                <a href="/demo" className="text-sm font-medium hover:text-indigo-400 transition-colors text-indigo-400">Run Demo</a>
              </div>
            </div>
          </div>
        </nav>
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {children}
        </main>
        <Toaster theme="dark" position="bottom-right" />
      </body>
    </html>
  );
}
    """,
    "app/page.tsx": """
import React from 'react';

export default function Home() {
  return (
    <div className="space-y-12">
      <div className="text-center space-y-4 py-20 border-b border-slate-800">
        <h1 className="font-display text-5xl font-bold tracking-tight text-white">
          The <span className="text-indigo-400">Agent</span> Economy is Here
        </h1>
        <p className="text-slate-400 text-lg max-w-2xl mx-auto">
          Discover, negotiate, and execute autonomous AI services using x402 payments and Algorand escrow.
        </p>
      </div>
      <div>
        <h2 className="text-2xl font-display font-semibold mb-6">Discovery Marketplace</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
           <div className="p-6 rounded-2xl bg-slate-800/50 border border-slate-700 hover:border-indigo-500/50 transition-colors">
              <div className="flex justify-between items-start mb-4">
                 <h3 className="font-bold text-lg">Loading Agents...</h3>
                 <span className="px-2 py-1 rounded text-xs bg-indigo-500/20 text-indigo-300">Data</span>
              </div>
              <p className="text-sm text-slate-400 mb-6">Fetching marketplace data from backend...</p>
              <div className="flex items-center justify-between text-sm">
                 <span className="font-medium text-slate-300">Trust: --</span>
                 <span className="font-medium text-white">-- ALGO</span>
              </div>
           </div>
        </div>
      </div>
    </div>
  );
}
    """,
    "app/dashboard/page.tsx": """
import React from 'react';

export default function Dashboard() {
  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-display font-bold">Agent Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="p-6 rounded-2xl bg-slate-800 border border-slate-700">
           <p className="text-sm text-slate-400">Total Revenue</p>
           <p className="text-3xl font-display font-bold mt-2">1,250 ALGO</p>
        </div>
        <div className="p-6 rounded-2xl bg-slate-800 border border-slate-700">
           <p className="text-sm text-slate-400">Trust Score</p>
           <p className="text-3xl font-display font-bold mt-2 text-green-400">95.5</p>
        </div>
        <div className="p-6 rounded-2xl bg-slate-800 border border-slate-700">
           <p className="text-sm text-slate-400">Active Escrows</p>
           <p className="text-3xl font-display font-bold mt-2">3</p>
        </div>
      </div>
    </div>
  );
}
    """,
    "app/demo/page.tsx": """
"use client";
import React, { useState } from 'react';
import { toast } from 'sonner';
import { motion, AnimatePresence } from 'framer-motion';
import { Play, CheckCircle2, CircleDashed, Server, CreditCard, Lock, Zap, ShieldCheck } from 'lucide-react';
import axios from 'axios';

const STAGES = [
  { id: 'discovery', label: 'Discovery', icon: Server },
  { id: 'negotiation', label: 'AI Negotiation', icon: Zap },
  { id: '402_payment', label: 'x402 Protocol', icon: CreditCard },
  { id: 'escrow_lock', label: 'Algorand Escrow', icon: Lock },
  { id: 'execution', label: 'Execution', icon: Play },
  { id: 'escrow_release', label: 'Settlement', icon: CheckCircle2 },
  { id: 'reputation', label: 'Trust Update', icon: ShieldCheck }
];

export default function DemoRunner() {
  const [running, setRunning] = useState(false);
  const [currentStageIndex, setCurrentStageIndex] = useState(-1);
  const [logs, setLogs] = useState<{stage: string, message: string}[]>([]);

  const runDemo = async () => {
    setRunning(true);
    setCurrentStageIndex(0);
    setLogs([]);
    
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const res = await axios.post(`${apiUrl}/api/demo/scenario`);
      const pipeline = res.data.pipeline;
      
      for (let i = 0; i < pipeline.length; i++) {
        const step = pipeline[i];
        setCurrentStageIndex(i);
        setLogs(prev => [...prev, { stage: step.step, message: step.message }]);
        
        toast(step.message, {
          description: `Stage: ${STAGES[i].label}`,
          icon: React.createElement(STAGES[i].icon, { className: "w-4 h-4 text-indigo-400" }),
        });
        
        // Wait 1.5s between steps to make it visible
        await new Promise(r => setTimeout(r, 1500));
      }
      
      toast.success("Demo Scenario Completed Successfully!");
      setCurrentStageIndex(STAGES.length);
    } catch (error) {
      toast.error("Demo failed to run. Is the backend up?");
      setCurrentStageIndex(-1);
    } finally {
      setRunning(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <div className="flex items-center justify-between">
        <div>
           <h1 className="text-3xl font-display font-bold">Automated Demo Runner</h1>
           <p className="text-slate-400 mt-2">Watch a complete agent-to-agent transaction in real-time.</p>
        </div>
        <button 
          onClick={runDemo} 
          disabled={running}
          className="px-6 py-3 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white rounded-lg font-medium flex items-center gap-2 transition-all shadow-[0_0_20px_rgba(79,70,229,0.3)] hover:shadow-[0_0_30px_rgba(79,70,229,0.5)]"
        >
          <Play className="w-5 h-5" />
          {running ? 'Running...' : 'Run Full Pipeline'}
        </button>
      </div>
      
      <div className="relative pt-12 pb-8">
        <div className="absolute top-16 left-0 w-full h-1 bg-slate-800 rounded-full" />
        <div className="relative flex justify-between">
          {STAGES.map((stage, idx) => {
             const Icon = stage.icon;
             const isPast = idx < currentStageIndex;
             const isCurrent = idx === currentStageIndex;
             const isFuture = idx > currentStageIndex;
             
             return (
               <div key={stage.id} className="flex flex-col items-center gap-3 relative z-10">
                 <motion.div 
                   animate={{
                     backgroundColor: isPast ? '#4f46e5' : isCurrent ? '#312e81' : '#1e293b',
                     borderColor: isPast ? '#4f46e5' : isCurrent ? '#818cf8' : '#334155',
                     scale: isCurrent ? 1.2 : 1
                   }}
                   className="w-10 h-10 rounded-full border-2 flex items-center justify-center shadow-xl"
                 >
                   <Icon className={`w-5 h-5 ${isPast ? 'text-white' : isCurrent ? 'text-indigo-400' : 'text-slate-500'}`} />
                 </motion.div>
                 <span className={`text-xs font-medium ${isPast || isCurrent ? 'text-slate-200' : 'text-slate-500'}`}>
                   {stage.label}
                 </span>
               </div>
             );
          })}
        </div>
      </div>
      
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 font-mono text-sm h-64 overflow-y-auto">
        <div className="text-slate-500 mb-4">// Transaction Log</div>
        <AnimatePresence>
          {logs.map((log, i) => (
            <motion.div 
              key={i}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              className="mb-2"
            >
              <span className="text-indigo-400">[{log.stage}]</span> <span className="text-slate-300">{log.message}</span>
            </motion.div>
          ))}
        </AnimatePresence>
        {!running && logs.length === 0 && (
          <div className="text-slate-600 italic">Click "Run Full Pipeline" to start...</div>
        )}
      </div>
    </div>
  );
}
    """
}

for rel_path, content in files.items():
    full_path = os.path.join(base, rel_path.replace("/", "\\"))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content.strip() + "\n")

print("Frontend files generated.")

import React, { useRef, useEffect } from 'react';
import { Chart, registerables } from 'chart.js';
import 'chartjs-adapter-date-fns';

Chart.register(...registerables);

export default function AdvancedChart({ data, predictions }) {
  const chartRef = useRef(null);
  
  useEffect(() => {
    if (!data || data.length === 0) return;
    
    const ctx = chartRef.current.getContext('2d');
    const chart = new Chart(ctx, {
      type: 'line',
      data: {
        datasets: [
          {
            label: 'Historical Prices',
            data: data.map(d => ({ x: new Date(d.date), y: d.close })),
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
          },
          {
            label: 'XGBoost Forecast',
            data: predictions.xgboost,
            borderColor: 'rgb(255, 99, 132)',
            borderDash: [5, 5],
            pointRadius: 0
          },
          {
            label: 'LSTM Forecast',
            data: predictions.lstm,
            borderColor: 'rgb(54, 162, 235)',
            borderDash: [5, 5],
            pointRadius: 0
          }
        ]
      },
      options: {
        responsive: true,
        scales: {
          x: {
            type: 'time',
            time: {
              unit: 'day',
              tooltipFormat: 'PPP'
            },
            title: { display: true, text: 'Date' }
          },
          y: {
            title: { display: true, text: 'Price (NPR)' }
          }
        },
        plugins: {
          annotation: {
            annotations: {
              buySignal: {
                type: 'line',
                yMin: data[data.length-1].close,
                yMax: data[data.length-1].close,
                borderColor: 'green',
                borderWidth: 2,
                label: {
                  content: 'Current Price',
                  position: 'end'
                }
              }
            }
          },
          tooltip: {
            mode: 'index',
            intersect: false,
            callbacks: {
              label: (context) => {
                let label = context.dataset.label || '';
                if (label) label += ': ';
                if (context.parsed.y !== null) {
                  label += `NPR ${context.parsed.y.toFixed(2)}`;
                }
                return label;
              }
            }
          }
        }
      }
    });
    
    return () => chart.destroy();
  }, [data, predictions]);
  
  return <canvas ref={chartRef} />;
}
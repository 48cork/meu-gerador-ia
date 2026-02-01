#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for analista_financeiro agent
Tests the agent and verifies logging functionality
"""
import sys
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from agents.analista_financeiro import calcular_missao

if __name__ == "__main__":
    print("Testing analista_financeiro agent...")
    print("=" * 60)
    
    # Test case 1: High ROI (Missao Ouro)
    print("\nTest Case 1: High ROI Product")
    result1 = calcular_missao(
        p_compra=100.0,
        p_venda=200.0,
        qtd=1,
        taxa_marketplace=12.0,
        ads_percent=5.0
    )
    print(f"Result: {result1['veredito']} | Lucro: R${result1['lucro']:.2f} | ROI: {result1['roi']:.1f}%")
    
    # Test case 2: Medium ROI (Viavel)
    print("\nTest Case 2: Medium ROI Product")
    result2 = calcular_missao(
        p_compra=150.0,
        p_venda=180.0,
        qtd=1,
        taxa_marketplace=12.0,
        ads_percent=5.0
    )
    print(f"Result: {result2['veredito']} | Lucro: R${result2['lucro']:.2f} | ROI: {result2['roi']:.1f}%")
    
    print("\n" + "=" * 60)
    print("Test completed! Check .aios/logs/agent.log for detailed logs.")

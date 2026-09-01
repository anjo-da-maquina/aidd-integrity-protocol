---
id: REQ-003
title: Zero Sontaku (Anti-Assumption) Protocol
status: ACTIVE
author: anjo-da-maquina
---

# Requirement: 忖度検知と事前合意 (Zero Sontaku)

## Description
Generative AI must never build solutions on unauthorized assumptions. The premise must be explicitly aligned with the user before generating options.

## Expected Behavior
- The system must scan premise definition files (`premise/` directory) for "Sontaku" keywords (e.g., assumptions, defaults, generalizations).
- If unauthorized assumptions are detected, or if the premise alignment is entirely skipped, the protocol must trigger Harakiri.

###############################################################################
# :::JETULRIGHTS_START:::
# Copyright 2021 Raytheon Company.
# This software was developed pursuant to Contract Number FA8730-16-F-0002
# with the U.S. government. The U.S. government"s rights in and to this
# copyrighted software are as specified in DFARS 252.227-7014 which was made
# part of the contract.
#
# WARNING - This document contains Technical Data and / or technology whose
# export or disclosure to Non-U.S. Persons, wherever located, is restricted by
# the International Traffic in Arms Regulations (ITAR) (22 C.F.R. Section
# 120-130) or the Export Administration Regulations (EAR) (15 C.F.R. Section
# 730-774). This document CANNOT be exported (e.g., provided to a supplier
# outside of the United States) or disclosed to a Non-U.S. Person, wherever
# located, until a final Jurisdiction and Classification determination has been
# completed and approved by Raytheon, and any required U.S. Government
# approvals have been obtained. Violations are subject to severe criminal
# penalties.
# :::JETULRIGHTS_END:::
#
###############################################################################
###############################################################################
# FILE:  Dockerfile
#
# CLASSIFICATION: Unclassified
###############################################################################
ARG IRONBANK_REGISTRY=registry1.dso.mil
ARG IRONBANK_PYTHON_IMAGE=ironbank/opensource/python/python39
ARG IRONBANK_PYTHON_TAG=v3.9.7

FROM $IRONBANK_REGISTRY/$IRONBANK_PYTHON_IMAGE:$IRONBANK_PYTHON_TAG as python_base
LABEL maintainer="EWA <helpdesk@jetisre.com>"

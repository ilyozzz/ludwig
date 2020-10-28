#! /usr/bin/env python
# coding=utf-8
# Copyright (c) 2020 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from ludwig.backend.base import Backend, LocalBackend


LOCAL_BACKEND = LocalBackend()


def get_local_backend():
    return LOCAL_BACKEND


def create_dask_backend():
    from ludwig.backend.dask import DaskBackend
    return DaskBackend()


backend_registry = {
    'dask': create_dask_backend,
    'local': get_local_backend,
    None: get_local_backend,
}


def create_backend(name):
    return backend_registry[name]()
# Copyright (c) 2021 Denys Makogon. All rights reserved.
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

# ip a | grep ether | awk '{print $2}'

import os

from id_lib import id


def test_hardware_address_in_id():
    idg = id.ObjectID()
    new_id = idg.get()
    hw_addr = (
        os.popen("""ip a | grep ether | awk '{print $2}'""")
        .read()
        .replace(":", "")
        .upper()
    )
    parts = hw_addr.split("\n")
    if len(parts) > 1:
        hw_addr = parts[0]

    assert hw_addr in new_id

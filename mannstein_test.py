# coding=utf-8
# Copyright 2021 The Landsat Contrails Dataset Authors.
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

"""Tests for mannstein."""

from absl.testing import absltest

from landsat_contrails_dataset import mannstein


class MannsteinTest(absltest.TestCase):

  # TODO: open source our end to end test.

  def test_get_angles(self):
    num_angles = 16
    config = {'num_line_kernels': num_angles}
    self.assertLen(mannstein.get_angles(config), num_angles)


if __name__ == '__main__':
  absltest.main()

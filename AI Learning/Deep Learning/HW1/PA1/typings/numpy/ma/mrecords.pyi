"""
This type stub file was generated by pyright.
"""

import numpy as np
import numpy.ma as ma
from numpy.ma import MaskedArray
from typing import Any, Optional

""":mod:`numpy.ma..mrecords`

Defines the equivalent of :class:`numpy.recarrays` for masked arrays,
where fields can be accessed as attributes.
Note that :class:`numpy.ma.MaskedArray` already supports structured datatypes
and the masking of individual fields.

.. moduleauthor:: Pierre Gerard-Marchant

"""
_byteorderconv = np.core.records._byteorderconv
_check_fill_value = ma.core._check_fill_value
__all__ = ['MaskedRecords', 'mrecarray', 'fromarrays', 'fromrecords', 'fromtextfile', 'addfield']
reserved_fields = ['_data', '_mask', '_fieldmask', 'dtype']
def _checknames(descr, names: Optional[Any] = ...):
    """
    Checks that field names ``descr`` are not reserved keywords.

    If this is the case, a default 'f%i' is substituted.  If the argument
    `names` is not None, updates the field names to valid names.

    """
    ...

def _get_fieldmask(self):
    ...

class MaskedRecords(MaskedArray, object):
    """

    Attributes
    ----------
    _data : recarray
        Underlying data, as a record array.
    _mask : boolean array
        Mask of the records. A record is masked when all its fields are
        masked.
    _fieldmask : boolean recarray
        Record array of booleans, setting the mask of each individual field
        of each record.
    _fill_value : record
        Filling values for each field.

    """
    def __new__(cls, shape, dtype: Optional[Any] = ..., buf: Optional[Any] = ..., offset=..., strides: Optional[Any] = ..., formats: Optional[Any] = ..., names: Optional[Any] = ..., titles: Optional[Any] = ..., byteorder: Optional[Any] = ..., aligned: bool = ..., mask=..., hard_mask: bool = ..., fill_value: Optional[Any] = ..., keep_mask: bool = ..., copy: bool = ..., **options):
        ...
    
    def __array_finalize__(self, obj):
        ...
    
    def _getdata(self):
        """
        Returns the data as a recarray.

        """
        ...
    
    _data = ...
    def _getfieldmask(self):
        """
        Alias to mask.

        """
        ...
    
    _fieldmask = ...
    def __len__(self):
        """
        Returns the length

        """
        ...
    
    def __getattribute__(self, attr):
        ...
    
    def __setattr__(self, attr, val):
        """
        Sets the attribute attr to the value val.

        """
        ...
    
    def __getitem__(self, indx):
        """
        Returns all the fields sharing the same fieldname base.

        The fieldname base is either `_data` or `_mask`.

        """
        ...
    
    def __setitem__(self, indx, value):
        """
        Sets the given record to value.

        """
        ...
    
    def __str__(self):
        """
        Calculates the string representation.

        """
        ...
    
    def __repr__(self):
        """
        Calculates the repr representation.

        """
        ...
    
    def view(self, dtype: Optional[Any] = ..., type: Optional[Any] = ...):
        """
        Returns a view of the mrecarray.

        """
        ...
    
    def harden_mask(self):
        """
        Forces the mask to hard.

        """
        ...
    
    def soften_mask(self):
        """
        Forces the mask to soft

        """
        ...
    
    def copy(self):
        """
        Returns a copy of the masked record.

        """
        ...
    
    def tolist(self, fill_value: Optional[Any] = ...):
        """
        Return the data portion of the array as a list.

        Data items are converted to the nearest compatible Python type.
        Masked values are converted to fill_value. If fill_value is None,
        the corresponding entries in the output list will be ``None``.

        """
        ...
    
    def __getstate__(self):
        """Return the internal state of the masked array.

        This is for pickling.

        """
        ...
    
    def __setstate__(self, state):
        """
        Restore the internal state of the masked array.

        This is for pickling.  ``state`` is typically the output of the
        ``__getstate__`` output, and is a 5-tuple:

        - class name
        - a tuple giving the shape of the data
        - a typecode for the data
        - a binary string for the data
        - a binary string for the mask.

        """
        self.fill_value = ...
    
    def __reduce__(self):
        """
        Return a 3-tuple for pickling a MaskedArray.

        """
        ...
    


def _mrreconstruct(subtype, baseclass, baseshape, basetype):
    """
    Build a new MaskedArray from the information stored in a pickle.

    """
    ...

mrecarray = MaskedRecords
def fromarrays(arraylist, dtype: Optional[Any] = ..., shape: Optional[Any] = ..., formats: Optional[Any] = ..., names: Optional[Any] = ..., titles: Optional[Any] = ..., aligned: bool = ..., byteorder: Optional[Any] = ..., fill_value: Optional[Any] = ...):
    """
    Creates a mrecarray from a (flat) list of masked arrays.

    Parameters
    ----------
    arraylist : sequence
        A list of (masked) arrays. Each element of the sequence is first converted
        to a masked array if needed. If a 2D array is passed as argument, it is
        processed line by line
    dtype : {None, dtype}, optional
        Data type descriptor.
    shape : {None, integer}, optional
        Number of records. If None, shape is defined from the shape of the
        first array in the list.
    formats : {None, sequence}, optional
        Sequence of formats for each individual field. If None, the formats will
        be autodetected by inspecting the fields and selecting the highest dtype
        possible.
    names : {None, sequence}, optional
        Sequence of the names of each field.
    fill_value : {None, sequence}, optional
        Sequence of data to be used as filling values.

    Notes
    -----
    Lists of tuples should be preferred over lists of lists for faster processing.

    """
    ...

def fromrecords(reclist, dtype: Optional[Any] = ..., shape: Optional[Any] = ..., formats: Optional[Any] = ..., names: Optional[Any] = ..., titles: Optional[Any] = ..., aligned: bool = ..., byteorder: Optional[Any] = ..., fill_value: Optional[Any] = ..., mask=...):
    """
    Creates a MaskedRecords from a list of records.

    Parameters
    ----------
    reclist : sequence
        A list of records. Each element of the sequence is first converted
        to a masked array if needed. If a 2D array is passed as argument, it is
        processed line by line
    dtype : {None, dtype}, optional
        Data type descriptor.
    shape : {None,int}, optional
        Number of records. If None, ``shape`` is defined from the shape of the
        first array in the list.
    formats : {None, sequence}, optional
        Sequence of formats for each individual field. If None, the formats will
        be autodetected by inspecting the fields and selecting the highest dtype
        possible.
    names : {None, sequence}, optional
        Sequence of the names of each field.
    fill_value : {None, sequence}, optional
        Sequence of data to be used as filling values.
    mask : {nomask, sequence}, optional.
        External mask to apply on the data.

    Notes
    -----
    Lists of tuples should be preferred over lists of lists for faster processing.

    """
    ...

def _guessvartypes(arr):
    """
    Tries to guess the dtypes of the str_ ndarray `arr`.

    Guesses by testing element-wise conversion. Returns a list of dtypes.
    The array is first converted to ndarray. If the array is 2D, the test
    is performed on the first line. An exception is raised if the file is
    3D or more.

    """
    ...

def openfile(fname):
    """
    Opens the file handle of file `fname`.

    """
    ...

def fromtextfile(fname, delimitor: Optional[Any] = ..., commentchar=..., missingchar=..., varnames: Optional[Any] = ..., vartypes: Optional[Any] = ...):
    """
    Creates a mrecarray from data stored in the file `filename`.

    Parameters
    ----------
    fname : {file name/handle}
        Handle of an opened file.
    delimitor : {None, string}, optional
        Alphanumeric character used to separate columns in the file.
        If None, any (group of) white spacestring(s) will be used.
    commentchar : {'#', string}, optional
        Alphanumeric character used to mark the start of a comment.
    missingchar : {'', string}, optional
        String indicating missing data, and used to create the masks.
    varnames : {None, sequence}, optional
        Sequence of the variable names. If None, a list will be created from
        the first non empty line of the file.
    vartypes : {None, sequence}, optional
        Sequence of the variables dtypes. If None, it will be estimated from
        the first non-commented line.


    Ultra simple: the varnames are in the header, one line"""
    ...

def addfield(mrecord, newfield, newfieldname: Optional[Any] = ...):
    """Adds a new field to the masked record array

    Uses `newfield` as data and `newfieldname` as name. If `newfieldname`
    is None, the new field name is set to 'fi', where `i` is the number of
    existing fields.

    """
    ...

